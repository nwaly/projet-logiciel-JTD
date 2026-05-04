"""liens back-end <=> front-end avec Flask pour journal"""
from flask import Blueprint, request, jsonify
from Controler.Tables.Journal import Journal
from Controler.base_de_donnee import Base

journal_flask = Blueprint("journal", __name__)
base = Base()
journal = Journal(base)

@journal_flask.route("/journal", methods=["POST"])
def ajoute_journal():
    """ajoute un element à journal"""
    body = request.json
    titre = body.get("titre")
    contenu = body.get("contenu")
    journal.nouveau(titre, contenu)

@journal_flask.route("/journal", methods=["GET"])
def get_journal():
    """va cherhcer toutes les données de journal dans la base et l'es envoie en json"""
    data_journal = journal.get_tout()
    return jsonify(data_journal)

@journal_flask.route('/journal/<int:id_>', methods=['PUT']) # front end=doit donner l'id qu'il veut
def update_journal(id_):
    """modifie un element de journal selon son id"""
    body = request.json
    contenu = body.get("contenu")
    modification = body.get("modification")  # format "YYYY-MM-DD"
    journal.modifier(contenu, modification, id_)
