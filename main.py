from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")


@app.route("/settings")
def render_settings():
    return render_template("settings.html")

@app.route("/journal")
def render_journal():
    return render_template("journal.html")

def main():
    app.run(debug=True)

if __name__ == "__main__":
    main()