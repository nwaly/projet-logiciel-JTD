from flask import Flask, render_template, url_for, request, jsonify
"""from flask_mysqldb import MySQL"""

app = Flask(__name__)

"""pour lier flask à la base de données SQL"""
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'flask'

"""mysql = MySQL(app)"""

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

# test de setup pour le système de forms php
@app.route("/submit_form", methods=['POST'])
def submit_form():
    data = request.form
    return {
        'titre'     : data['titre'],
        'entrée' : data['contenu'],
    }

def main():
    app.run(debug=True)

if __name__ == "__main__":
    main()