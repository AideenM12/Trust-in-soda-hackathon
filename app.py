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
@app.route("/home")
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
                    "profile", username=session["user"]))
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
    if session["user"]:
        return render_template("profile.html", username=username)

    return redirect(url_for("login"))


@app.route("/requirements")
def requirements():
    return render_template("requirements-survey.html")


@app.route("/subcategories")
def subcategories():
    return render_template("disabilities-subcategories.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")

# Error handlers

@app.errorhandler(404)
def page_not_found(error):
    """
    Error handler to display unique message for error 404.
    """
    error = 404
    error_msg = "I'm sorry but the page you looking for doesn't exist!"
    return render_template("error.html", error=error, error_msg=error_msg), 404


@app.errorhandler(500)
def internal_error(error):
    """
    Error handler to display unique message for error 500.
    """
    error = 500
    error_msg = "We're sorry! There is an internal server error.\
        please try again later."
    return render_template(
        "error.html",
        error=error,
        error_msg=error_msg), 500


@app.errorhandler(Exception)
def other_exceptions(error):
    """
    Error handler to display message for errors other then 404 and 500.
    """
    error_msg = "We're sorry but the error above has occurred"
    return render_template("error.html", error=error, error_msg=error_msg)

# Change to False before submission
if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
