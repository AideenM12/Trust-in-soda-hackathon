import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from flask_wtf.csrf import CSRFProtect, validate_csrf, ValidationError
from wtforms import (
    Form, TextField,
    PasswordField, validators)
from wtforms.validators import InputRequired, EqualTo


if os.path.exists("env.py"):
    import env


app = Flask(__name__)
csrf = CSRFProtect(app)


csrf.init_app(app)


app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")


mongo = PyMongo(app)


@app.route("/")
@app.route("/index")
def index():
    """
    Renders home page when main website loaded.
    """
    return render_template("index.html")


@app.route("/test")
def test():
    test_collection = list(mongo.db.test_collection.find())
    return render_template("test.html", test_collection=test_collection)


"""
The below code was taken from
https://wtforms.readthedocs.io/en/stable/crash_course/
"""


class LoginForm(Form):
    """
    Form fields for user login
    """
    username = TextField('Username')
    password = PasswordField('Password')


"""
End Credit
"""

"""
The below code was found on
https://pythonprogramming.net/flask-registration-tutorial/
"""


class RegistrationForm(Form):
    """
    Form fields and validators for registration,
    WTForms is used to validate the registration form fields.
    """
    username = TextField('Username',
                         [validators.Length(min=4, max=20,
                          message="Username max length 20 characters"),
                          validators.Regexp(r'^\w+$', message=(
                              "Username must contain only letters "
                              "numbers or underscore"))])

    email = TextField('Email Address', [validators.Length(min=6, max=50)])

    password = PasswordField('Password', [
        validators.InputRequired(),
        validators.Regexp(r'^\w+$', message=(
            "Password must contain only letters numbers or underscore"))
    ])


"""
End Credit
"""


@app.route("/registration", methods=["GET", "POST"])
def registration():
    """
    Allows users to sign up to the site, create an account profile
    and send data to the database
    """
    try:
        form = RegistrationForm(request.form)

        if request.method == 'POST' and form.validate():
            existing_user = mongo.db.users.find_one(
                {"username": request.form.get("username").lower()})

            if existing_user:
                flash("Username already exists")
                return redirect(url_for("login"))

            signup = {
                "username": request.form.get("username").lower(),
                "email": request.form.get("email").lower(),
                "password": generate_password_hash(
                    request.form.get("password")),
                "first_name": "",
                "last_name": "",
                "preferred_pronouns": "",
                "date_of_birth": "",
                "number_and_street_name": "",
                "locality_name": "",
                "town": "",
                "postcode": "",
                "visual": "",
                "auditory": "",
                "physical": "",
                "cognitive": "",
                "speech": "",
                "other": "",
                "none": ""
            }
            mongo.db.users.insert_one(signup)

            session["user"] = request.form.get("username").lower()
            flash('You have signed up successfully!')
            return redirect(url_for("login"))

        return render_template('newprofile.html', form=form)

    except Exception as e:
        return (str(e))


@app.route("/login", methods=["GET", "POST"])
def login():
    """
    Allows users to login and access their profile
    by checking their password and username to make sure
    it corresponds with the users collection in the database.
    """
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()

                flash("Welcome back {}!".format(
                    request.form.get("username")))
                return redirect(url_for(
                    "requirements"))
            else:
                flash("Incorrect Username/password, Please try again")
                return redirect(url_for("login"))

        else:
            flash("Incorrect Username/password, Please try again")
            return redirect(url_for("login"))

    return render_template("login.html", title='Login', form=form)


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    """
    Links users to their profiles by checking the session username
    against the users collection in the database. Profile page
    displays all the user's contributions upon successful
    log in.
    """
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    user = mongo.db.users.find_one({'username': session['user']})
    username = user['username']
    first_name = user['first_name']
    last_name = user['last_name']
    preferred_pronouns = user['preferred_pronouns']
    date_of_birth = user['date_of_birth']
    number_and_street_name = user['number_and_street_name']
    locality_name = user['locality_name']
    town = user['town']
    postcode = user['postcode']
    visual = user['visual']
    auditory = user['auditory']
    physical = user['physical']
    cognitive = user['cognitive']
    speech = user['speech']
    other = user['other']
    none = user['none']
    if session["user"]:
        return render_template("profile.html", username=username,
                               first_name=first_name, user=user,
                               last_name=last_name, preferred_pronouns=preferred_pronouns,
                               date_of_birth=date_of_birth, number_and_street_name=number_and_street_name,
                               locality_name=locality_name, town=town, postcode=postcode,
                               visual=visual, auditory=auditory, physical=physical,
                               cognitive=cognitive, speech=speech, other=other, none=none)

    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    """
    Allows users to logout of their profile
    by removing users from session cookie and redirects
    to log in page.
    """
    flash("You have logged out successfully!")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/requirements")
def requirements():
    return render_template("requirements-survey.html")


@app.route('/insert_profile', methods=['GET', 'POST'])
def insert_profile():
    """
    Take user input from requirements from
    and insert into profile collection
    """
    if request.method == "POST":
        visual = "true" if request.form.get("visual") else "false"
        auditory = "true" if request.form.get("auditory") else "false"
        physical = "true" if request.form.get("physical") else "false"
        cognitive = "true" if request.form.get("cognitive") else "false"
        speech = "true" if request.form.get("speech") else "false"
        other = "true" if request.form.get("other") else "false"
        other_impairments = "true" if request.form.get(
            "other_impairments") else "false"
        none = "true" if request.form.get("none") else "false"
        user = mongo.db.users
        # Resource: Set Operator -
        # https://docs.mongodb.com/manual/reference/operator/update/set/
        user.update(
            {"username": session["user"]},
            {"$set":
                {'first_name': request.form['first_name'],
                 'last_name': request.form['last_name'],
                 'preferred_pronouns': request.form['preferred_pronouns'],
                 'date_of_birth': request.form['date_of_birth'],
                 'number_and_street_name': request.form['number_and_street_name'],
                 'locality_name': request.form['locality_name'],
                 'town': request.form['town'],
                 'postcode': request.form['postcode'],
                 'visual': visual,
                 'auditory': auditory,
                 'physical': physical,
                 'cognitive': cognitive,
                 'speech': speech,
                 'other': other,
                 'other_impairments': other_impairments,
                 'none': none
                 }}
        )
        user = mongo.db.users.find_one({'username': session['user']})
        username = user['username']
        first_name = user['first_name']
        last_name = user['last_name']
        preferred_pronouns = user['preferred_pronouns']
        date_of_birth = user['date_of_birth']
        number_and_street_name = user['number_and_street_name']
        locality_name = user['locality_name']
        town = user['town']
        postcode = user['postcode']
        visual = user['visual']
        auditory = user['auditory']
        physical = user['physical']
        cognitive = user['cognitive']
        speech = user['speech']
        other = user['other']
        none = user['none']
        
        if session['user']:
            return render_template('profile.html', username=username,
                                   first_name=first_name, user=user,last_name=last_name, preferred_pronouns=preferred_pronouns,
                               date_of_birth=date_of_birth, number_and_street_name=number_and_street_name,
                               locality_name=locality_name, town=town, postcode=postcode,
                               visual=visual, auditory=auditory, physical=physical,
                               cognitive=cognitive, speech=speech, other=other, none=none)





@ app.route("/subcategories")
def subcategories():
    return render_template("subcategories.html")


@ app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        flash("Thanks {}, we have received your message!".format(
            request.form.get('name')))
    return render_template("contact.html")


# Error handlers


@ app.errorhandler(404)
def page_not_found(error):
    """
    Error handler to display unique message for error 404.
    """
    error=404
    error_msg="I'm sorry but the page you looking for doesn't exist!"
    return render_template("error.html", error = error,
                           error_msg = error_msg), 404


@ app.errorhandler(500)
def internal_error(error):
    """
    Error handler to display unique message for error 500.
    """
    error=500
    error_msg="We're sorry! There is an internal server error.\
        please try again later."
    return render_template(
        "error.html",
        error = error,
        error_msg = error_msg), 500


@ app.errorhandler(Exception)
def other_exceptions(error):
    """
    Error handler to display message for errors other then 404 and 500.
    """
    error_msg="We're sorry but the error above has occurred"
    return render_template("error.html", error = error, error_msg = error_msg)


# Change to False before submission
if __name__ == "__main__":
    app.run(host = os.environ.get("IP"),
            port = int(os.environ.get("PORT")),
            debug = True)
