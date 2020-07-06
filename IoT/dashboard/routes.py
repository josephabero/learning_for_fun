from flask import render_template, url_for, flash, redirect
from dashboard import app

posts = [
    {
        "author": "Joseph Abero",
        "title": "Blog Post 1",
        "content": "First post content",
        "date_posted": "June 29, 2020"
    },
    {
        "author": "Joseph Abero",
        "title": "Blog Post 2",
        "content": "Second post content",
        "date_posted": "June 30, 2020"
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", posts=posts)

@app.route("/about")
def about():
    return render_template("about.html", title="About")