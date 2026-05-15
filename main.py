from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html", title = "Home")

@app.route("/settings")
def render_settings():
    return render_template("settings.html", title = "Settings")

@app.route("/journal")
def render_journal():
    return render_template("journal.html", title = "Journal")

@app.route("/todo")
def render_todo():
    return render_template("todo.html", title = "To Do")

@app.route("/tracker")
def render_tracker():
    return render_template("tracker.html", title = "Tracker")

def main():
    app.run(debug=True)

if __name__ == "__main__":
    main()