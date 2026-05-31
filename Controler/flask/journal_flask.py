"""liens back-end <=> front-end avec Flask pour journal"""
from flask import Blueprint, request, jsonify
from Controler.Tables.Journal import Journal
from Controler.base_de_donnee import Base

journal_flask = Blueprint("journal", __name__)
base = Base()
journal = Journal(base)

# route à utiliser pour envoyer une entrée journal à la base
@journal_flask.route("/journal", methods=["POST"])
def ajoute_journal():
    """ajoute un element à journal"""
    body = request.json
    titre = body.get("titre")
    contenu = body.get("contenu")
    journal.nouveau(titre, contenu)
    return jsonify({"message": "Journal créé"}), 201

# route à utiliser pour récuperer toutes les entrées de journal (retourne un dictionnaire json)
@journal_flask.route("/journal", methods=["GET"])
def get_journal():
    """va chercher toutes les données de journal dans la base et les envoie en json"""
    data_journal = journal.get_tout()
    return jsonify(data_journal), 200

# route à utiliser pour modifier une entrée journal
@journal_flask.route('/journal/<int:id_>', methods=['PUT']) # front end=doit donner l'id qu'il veut
def update_journal(id_):
    """modifie un element de journal selon son id"""
    body = request.json
    contenu = body.get("contenu")
    modification = body.get("modification")  # format "YYYY-MM-DD"
    journal.modifier(contenu, modification, id_)
    return jsonify({"message": "Journal modifié"}), 201
