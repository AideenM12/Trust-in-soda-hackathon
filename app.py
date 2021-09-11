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
def hello():
    return "Hello World!"


@app.route("/profile", methods=["GET", "POST"])
def profile():
    """
    Links users to their profiles by checking the session username
    against the users collection in the database. Profile page
    displays all the user's contributions upon successful
    log in.
    """
       
    return render_template("profile.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/disability-subcategories")
def disability_subcategories():
    return render_template("disability-subcategories.html")


@app.route("/requirements-survey")
def requirements_survey():
    return render_template("requirements-survey.html")


# Change to False before submission
if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
