import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId



if os.path.exists("env.py"):
    import env

app = Flask(__name__)


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


@app.route("/profile", methods=["GET", "POST"])
def profile():
    """
    Links users to their profiles by checking the session username
    against the users collection in the database. Profile page
    displays all the user's contributions upon successful
    log in.
    """
       
    return render_template("profile.html")


@app.route("/requirements")
def requirements():
    return render_template("requirements-survey.html")


@app.route("/subcategories")
def subcategories():
    return render_template("disabilities-subcategories.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")



@app.errorhandler(500)
def server_error(error):
    return render_template("500.html", error=error), 500
    


@app.errorhandler(404)
def error404(e):
    return render_template('404.html'), 404



# Change to False before submission
if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
