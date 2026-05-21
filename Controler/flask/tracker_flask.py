"""liens back-end <=> front-end avec Flask pour Tracker"""
from flask import Blueprint, request, jsonify
from Controler.Tables.Tracker import Tracker
from Controler.Tables.calendrier import Calendrier
from Controler.Tables.calendrier_has_tracker import CalendrierHasTracker
from Controler.base_de_donnee import Base

tracker_flask = Blueprint("tracker", __name__)
calendrier_flask = Blueprint("calendrier", __name__)
calendrier_has_tracker_flask = Blueprint("calendrier_has_tracker", __name__)

base = Base()
tracker = Tracker(base)
calendrier = Calendrier(base)
calendrier_has_tracker = CalendrierHasTracker(base)

# route à utiliser pour ajouter un nouveau tracker
@tracker_flask.route("/tracker", methods=["POST"])
def ajoute_tracker():
    """ajoute un nouveau tracker"""
    body = request.json
    nom = body.get("nom")
    description = body.get("description")
    couleur = body.get("couleur")
    icone = body.get("icone")
    tracker.nouveau(nom, description, couleur, icone)
    return jsonify({"message": "Tracker ajouté"}), 201

# route à utiliser pour récuperer tout les éléments tracker
@tracker_flask.route("/tracker", methods=["GET"])
def get_tracker():
    """va cherhcer toutes les données des trackers dans la base et les envoie en json"""
    donnee_tracker = tracker.get_tout()
    return jsonify(donnee_tracker), 200

# route à utiliser pour ajouter un nouveau jour à calendrier
@calendrier_flask.route("/calendrier", methods=["POST"])
def creer_nouveau_jour():
    """crée un nouveau jour dans le calendrier"""
    date = request.json.get("date")
    calendrier.creer_jour(date)
    return jsonify({"message": "Jour créé"}), 201

# route à utiliser pour récuperer tout les tracker d'un jour
@calendrier_has_tracker_flask.route("/calendrier/<int:calendrier_id>/trackers", methods=["GET"])
def recupere_tracker_pour_jour(calendrier_id):
    """permet de récuperer tout les trackers d'un jour"""
    tracker_jour = calendrier_has_tracker.trouve_tracker_par_jour(calendrier_id)
    return jsonify(tracker_jour), 200

# route à utiliser pour activer / ou desactivé un tracker pour un jour donné
@calendrier_has_tracker_flask.route("/calendrier/<id>/tracker/<id>/activer_desactiver", methods=["PUT"])
def activer_desactiver_tracker(calendrier_id, tracker_id):
    """routes flask pour activer ou désactiver un tracker donné pour un jour donné"""
    tracker_jour = calendrier_has_tracker.trouve_tracker_par_jour(calendrier_id)
    statut = next((tracker ["Calendrier_has_Tracker_Statut"]
                   for tracker in tracker_jour if tracker["Tracker_ID"] == tracker_id), None)
    if statut is None:
        calendrier_has_tracker.activer_tracker(calendrier_id, tracker_id)
        return jsonify({"message": "Tracker activé"}), 201
    if statut == 1:
        calendrier_has_tracker.desactiver_tracker(calendrier_id, tracker_id)
        return jsonify({"message": "Tracker désactivé"}), 200
    calendrier_has_tracker.activer_tracker(calendrier_id, tracker_id)
    return jsonify({"message": "Tracker activé"}), 201
