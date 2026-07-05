from flask import Flask, render_template
from datetime import datetime

# Initialize the Flask application
app = Flask(__name__)


from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    flash,
    jsonify,
    send_from_directory,
)
from datetime import datetime
import os

# Initialize the Flask application. Example shows explicit static folder.
app = Flask(__name__, static_folder="static", static_url_path="/static")
app.secret_key = os.environ.get("FLASK_SECRET", "dev-secret")


@app.context_processor
def inject_now():
    return {"current_year": datetime.utcnow().year}


@app.route("/")
def hello_world():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/gallery")
def gallery():
    images = [
        f"https://via.placeholder.com/600x400?text=Image+{i}" for i in range(1, 9)
    ]
    return render_template("gallery.html", images=images)


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()
        message = request.form.get("message", "").strip()
        if not name or not email:
            flash("Name and email are required.", "error")
            return redirect(url_for("contact"))
        # For demo, we won't persist; just flash and redirect
        flash("Thanks for your message! We'll get back to you.", "success")
        return redirect(url_for("contact"))
    return render_template("contact.html")


@app.route("/assets/<path:filename>")
def assets(filename):
    # demonstrates serving from a different folder (assets/)
    return send_from_directory("assets", filename)


@app.route("/jinja-demo")
def jinja_demo():
    items = [
        {"name": "Apples", "qty": 5},
        {"name": "Oranges", "qty": 0},
        {"name": "Bananas", "qty": 12},
    ]
    return render_template("jinja_demo.html", items=items)


@app.route("/serve-static")
def serve_static_demo():
    # shows usage of url_for for static and assets
    return render_template("serve_static.html")


@app.route("/search")
def search():
    q = request.args.get("q", "")
    # demo: pretend we search and return results containing q
    results = [f"Result for {q} #{i}" for i in range(1, 4)] if q else []
    return render_template("search.html", q=q, results=results)


@app.route("/api/status")
def api_status():
    return jsonify({"status": "ok", "time": datetime.utcnow().isoformat() + "Z"})


@app.route("/course")
def course_index():
    modules = [
        ("Introduction to Flask", "intro", "3:15"),
        ("Creating our first Flask App", "first-app", "6:48"),
        ("Creating a Static Site", "static-site", "13:48"),
        ("Serving Static Files in Flask", "serve-static", "5:01"),
        ("Handling Forms in Flask", "contact", "10:05"),
        ("Jinja 2 Templating in Flask", "jinja-demo", "6:06"),
        ("Conditionals, Loops & Comments in Jinja2", "jinja-demo", "6:54"),
        ("Template Inheritance", "index", "10:24"),
        ("Changing static folder & url_for", "serve-static", "9:19"),
        ("Query Parameters in Flask", "search", "7:08"),
        ("Creating APIs in Flask using jsonify", "api_status", "3:40"),
        ("Message Flashing in Flask", "contact", "--"),
    ]
    return render_template("course.html", modules=modules)


if __name__ == "__main__":
    app.run(debug=True)
