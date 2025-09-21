from datetime import datetime
from flask import Blueprint, render_template, request, redirect, url_for, flash

bp = Blueprint("main", __name__)

def llll_format(dt: datetime) -> str:
    # Approximate a Moment.js 'LLLL' format using Python.
    # Example: Sunday, September 21, 2025 8:05 PM
    return dt.strftime("%A, %B %-d, %Y %-I:%M %p") if hasattr(dt, "strftime") else str(dt)

@bp.route("/", methods=["GET"])
def index():
    now = datetime.now()
    return render_template("index.html", now_str=llll_format(now))

@bp.route("/signup", methods=["GET", "POST"])
def signup():
    message = None
    user = None
    email = None

    if request.method == "POST":
        user = (request.form.get("name") or "").strip()
        email = (request.form.get("email") or "").strip()

        if "utoronto" in email.lower():
            message = "Thanks! Your UofT email was accepted."
        else:
            message = "Please use your UofT email address."

    return render_template("form.html", message=message, user=user, email=email)
