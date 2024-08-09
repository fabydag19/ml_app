from flask import Flask, render_template, request, session, render_template, redirect, url_for
import mysql.connector
import os
from model import model_predictions

app = Flask(__name__)

app.secret_key = "thesis"

# MySQL configuration
db_config = {
    "user": os.environ.get("DB_USER"),
    "password": os.environ.get("DB_PASSWORD"),
    "host": os.environ.get("DB_HOST"),
    "database": os.environ.get("DB_NAME"),
}


# Database connection
def get_db_connection():
    conn = mysql.connector.connect(**db_config)
    return conn


@app.route("/", methods=["GET", "POST"])
def login():
    msg = ""
    if (
        request.method == "POST"
        and "username" in request.form
        and "password" in request.form
    ):
        username = request.form["username"]
        password = request.form["password"]

        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute(
            "SELECT * FROM users WHERE username = %s AND password_hash = SHA2(%s, 256)",
            (username, password),
        )
        account = cursor.fetchone()

        if account:
            session["loggedin"] = True
            session["id"] = account["id"]
            session["username"] = account["username"]
            return redirect(url_for("home"))  # Redirige alla home page (index.html)
        else:
            msg = "Incorrect username or password!"

        cursor.close()
        conn.close()

    return render_template("login.html", msg=msg)


@app.route("/home", methods=["GET", "POST"])
def home():

    result = None
    if request.method == "POST":

        short_description = request.form.get("short_description")
        description = request.form.get("description")
        impact = int(request.form.get("impact"))
        urgency = int(request.form.get("urgency"))
        priority = int(request.form.get("priority"))

        result = model_predictions(
            short_description, description, impact, urgency, priority
        )

    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
