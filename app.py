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


@app.route("/requirements")
def requirements():
    return render_template("requirements-survey.html")


@app.route("/subcategories")
def subcategories():
    return render_template("disabilities-subcategories.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


# Change to False before submission
if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)