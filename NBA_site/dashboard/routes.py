from flask import render_template, url_for, flash, redirect, request
from nba_api.stats.static import teams
from dashboard import app

teams = teams.get_teams()

devices = [
    {
        "device_id": "1EF",
        "name": "ESPY",
        "type": "esp32",
        "connection_status": "Connected"
    },
    {
        "device_id": "2GF",
        "name": "Joseph SJ2",
        "type": "SJTwo",
        "connection_status": "Connected"
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", teams=teams)

@app.route("/about")
def about():
    return render_template("about.html", title="About")

@app.route("/team/<team_name>")
def team(team_name="NBA"):
    # team = teams[team_name]
    return render_template(f"team.html", team_name=team_name)