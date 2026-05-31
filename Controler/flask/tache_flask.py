"""liens back-end <=> front-end avec Flask pour journal"""
from flask import Blueprint, request, jsonify
from Controler.Tables.Tache import Tache, SousTache
from Controler.base_de_donnee import Base

tache_flask = Blueprint("tache", __name__)
base = Base()
tache = Tache(base)

# route à utiliser pour envoyer une nouvelle tache à la base
@tache_flask.route("/tache", methods=["POST"])
def ajoute_tache():
    """ajoute un element à la table tache"""
    body = request.json
    nom = body.get("nom")
    date = body.get("date")
    statut = body.get("statut")
    sous_tache = body.get("sous_tache")
    tache.nouveau(nom, date, statut, sous_tache)
    return jsonify({"message": "Tache ajoutée"}), 201

# route à utiliser pour récuperer toutes les taches 
@tache_flask.route("/tache", methods=["GET"])
def get_tache():
    """va chercher toutes les données de tache dans la base et les envoie en json"""
    data_tache = tache.get_tout()
    return jsonify(data_tache), 200


# route à utiliser pour modifier le statut d'une tâche
@tache_flask.route('/tache_statut', methods=['PUT'])
def update_statut_tache():
    """modifie le statut de tache selon son nom, sa date et son nouveau statut"""
    body = request.json
    nom = body.get("nom")
    date = body.get("date")
    statut = body.get("statut") # le nouveau statut
    tache.modification_statut(nom, date, statut)
    return jsonify({"message": "statut de la tache modifiée"}), 201

# route à utiliser pour modifier la date d'une tâche
@tache_flask.route('/tache_date', methods=['PUT'])
def update_date_tache():
    """modifie le statut de tache selon son nom, sa date et son nouveau statut"""
    body = request.json
    nom = body.get("nom")
    date = body.get("date")
    date_modification = body.get("date_modification") # la nouvelle date
    tache.modification_statut(nom, date, date_modification)
    return jsonify({"message": "date de la tache modifiée"}), 201

sous_taches_flask = Blueprint("sous_tache", __name__)
base = Base()
sous_taches = SousTache(base)

# # route à utiliser pour ajouter une sous-tache
@sous_taches_flask.route("/sous_tache", methods=["POST"])
def ajoute_sous_tache():
    """ajoute un element à la table sous_tache"""
    body = request.json
    nom = body.get("nom")
    statut = body.get("statut")
    tache_id = body.get("tache_id")
    sous_taches.nouveau(nom, statut, tache_id)
    return jsonify({"message": "sous_tache crée"}), 201

# route à utiliser pour récuperer toutes les sous taches
@sous_taches_flask.route("/sous_tache", methods=["GET"])
def get_sous_tache():
    """va cherhcer toutes les données de la sous-tache dans la base et les envoie en json"""
    data_sous_tache = sous_taches.get_tout()
    return jsonify(data_sous_tache), 200
