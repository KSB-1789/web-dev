from flask import Flask, render_template, redirect, url_for, request, session

# Create an instance of the Flask class
app = Flask(__name__)
app.secret_key = "xyz"

# Home page
@app.route("/")
def home():
    return render_template("index.html")

# Login page
@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        user = request.form["nm"]
        session["user"] = user
        return redirect(url_for("user"))
    else:
        return render_template("login.html")

# User page
@app.route("/user")
def user():
    if "user" in session:
        user = session["user"]
        return render_template("user.html", user=user)
    else:
        return redirect(url_for("login"))

# Logout route
@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)
