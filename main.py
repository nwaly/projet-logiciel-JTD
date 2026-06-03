from flask import Flask, render_template
from Controler.flask.journal_flask import journal_flask
from Controler.flask.parametre_flask import parametre_flask
from Controler.flask.tache_flask import tache_flask, Tache, SousTache
from Controler.flask.tracker_flask import tracker_flask
from flask_moment import Moment

app = Flask(__name__)
moment = Moment(app)

# enregistrer les blueprints dans l'app flask
app.register_blueprint(journal_flask)
app.register_blueprint(parametre_flask)
app.register_blueprint(tache_flask)
app.register_blueprint(tracker_flask)

# liens de navigation de pages html 
@app.route("/")
def hello_world():
    return render_template("index.html", title = "Home")

@app.route("/page_settings")
def render_settings():
    return render_template("settings.html", title = "Paramètres")

@app.route("/page_journal")
def render_journal():
    return render_template("journal.html", title = "Journal")

@app.route("/page_todo")
def render_todo():
    return render_template("todo.html", title = "To Do")

@app.route("/page_tracker")
def render_tracker():
    return render_template("tracker.html", title = "Tracker")

def main():
    app.run(debug=True)

if __name__ == "__main__":
    main()