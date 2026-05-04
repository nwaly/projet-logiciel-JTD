"""liens back-end <=> front-end avec Flask pour journal"""
from flask import Blueprint, request, jsonify
from Controler.Tables.Tache import Tache, SousTache
from Controler.base_de_donnee import Base

tache_flask = Blueprint("tache", __name__)
base = Base()
tache = Tache(base)

@tache_flask.route("/tache", methods=["POST"])
def ajoute_tache():
    """ajoute un element à la table tache"""
    body = request.json
    nom = body.get("nom")
    date = body.get("date")
    statut = body.get("statut")
    sous_tache = body.get("sous_tache")
    tache.nouveau(nom, date, statut, sous_tache)

@tache_flask.route("/tache", methods=["GET"])
def get_tache():
    """va cherhcer toutes les données de tache dans la base et les envoie en json"""
    data_tache = tache.get_tout()
    return jsonify(data_tache)

@tache_flask.route('/tache', methods=['PUT'])
def update_statut_journal():
    """modifie le statut de tache selon son nom, sa date et son nouveau statut"""
    body = request.json
    nom = body.get("nom")
    date = body.get("date")
    statut = body.get("statut") # le nouveau statut
    tache.modification_statut(nom, date, statut)

@tache_flask.route('/tache', methods=['PUT'])
def update_date_journal():
    """modifie le statut de tache selon son nom, sa date et son nouveau statut"""
    body = request.json
    nom = body.get("nom")
    date = body.get("date")
    date_modification = body.get("date_modification") # la nouvelle date
    tache.modification_statut(nom, date, date_modification)

sous_tache_flask = Blueprint("sous_tache", __name__)
base = Base()
sous_tache = SousTache(base)

@sous_tache_flask.route("/sous_tache", methods=["POST"])
def ajoute_sous_tache():
    """ajoute un element à la table sous_tache"""
    body = request.json
    nom = body.get("nom")
    statut = body.get("statut")
    tache_id = body.get("tache_id")
    sous_tache.nouveau(nom, statut, tache_id)

@sous_tache_flask.route("/sous_tache", methods=["GET"])
def get_sous_tache():
    """va cherhcer toutes les données de la sous-tache dans la base et les envoie en json"""
    data_sous_tache = sous_tache.get_tout()
    return jsonify(data_sous_tache)
