from flask import Flask, render_template
from  Controler.flask.journal_flask import journal_flask
from Controler.flask.parametre_flask import parametre_flask
from Controler.flask.tache_flask import tache_flask
from Controler.flask.tracker_flask import tracker_flask

app = Flask(__name__)

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
    return render_template("settings.html", title = "Settings")

@app.route("/page_journal")
def render_journal():
    return render_template("journal.html", title = "Journal")

@app.route("/page_todo")
def render_todo():
    return render_template("todo.html", title = "To Do")

@app.route("/page_tracker")
def render_tracker():
    return render_template("tracker.html", title = "Tracker")

"""
# fonctions
journal_entry_items = []

@app.route("/fonction-journal", methods=["GET", "POST"])
def ajoute_journal():
    titre = request.form["titre"]
    contenu = request.form["contenu"]
    journal_entry_items.extend(titre, contenu)
    journal.nouveau(titre, contenu)
    return jsonify({"message": "Journal crée"}), 201

# to do
todo_items = []

@app.route("/fonction-todo", methods=["GET", "POST"])
def ajoute_todo():
    todo = request.form["todo"]
    todo_items.extend(todo)
    return jsonify({"message": "Todo crée"}), 201
"""

# routes pour fonctions js
# au lieu d'utiliser la balise html 'form' (qui redirige toujours la page au lieu de rester sur celle où on est)
# utiliser une autre balise qui appelle une fonction js dans laquelle on fetch la fonction définie dans flask
# @app.route("/fonction-js", method="POST")


def main():
    app.run(debug=True)

if __name__ == "__main__":
    main()