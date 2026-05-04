"""liens back-end <=> front-end avec Flask pour Tracker"""
from flask import Blueprint, request, jsonify
from Controler.Tables.Tracker import Tracker
from Controler.base_de_donnee import Base

tracker_flask = Blueprint("tracker", __name__)
base = Base()
tracker = Tracker(base)

@tracker_flask.route("/tracker", methods=["POST"])
def ajoute_tracker():
    """ajoute un element à tracker"""
    body = request.json
    nom = body.get("nom")
    description = body.get("description")
    couleur = body.get("couleur")
    icone = body.get("icone")
    tracker.nouveau(nom, description, couleur, icone)

@tracker_flask.route("/tracker", methods=["GET"])
def get_tracker():
    """va cherhcer toutes les données de tracker dans la base et les envoie en json"""
    data_tracker = tracker.get_tout()
    return jsonify(data_tracker)
