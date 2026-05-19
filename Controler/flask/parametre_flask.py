"""liens back-end <=> front-end avec Flask pour parametre"""
from flask import Blueprint, request, jsonify
from Controler.Tables.parametres import Parametres
from Controler.base_de_donnee import Base

parametre_flask = Blueprint("parametre", __name__)
base = Base()
parametre = Parametres(base)

@parametre_flask.route("/parametre", methods=["GET"])
def get_parametre():
    """va cherhcer toutes les données de parametre dans la base et les envoie en json"""
    data_parametre = parametre.get_tout()
    return jsonify(data_parametre), 200

@parametre_flask.route('/parametre', methods=['PUT'])
def update_affichage_parametre():
    """modifie le statut du parametre d'affichage"""
    body = request.json
    affichage = body.get("affichage")
    parametre.modifier_affichage(affichage)
    return jsonify({"message": "statut de parametre modifié"}), 201

@parametre_flask.route('/parametre', methods=['PUT'])
def update_couleur_parametre():
    """modifie le statut des couleurs de parametre"""
    body = request.json
    couleur = body.get("couleur")
    parametre.modifier_couleur(couleur)
    return jsonify({"message": "couleur de parametres modifié"}), 201
