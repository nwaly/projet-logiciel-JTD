"""Table Parametres"""

import json


class Parametres :
    """classe Parametres : Parametres_ID, Parametres_affichage, Parametres_couleur"""
    def __init__(self, base):
        self.base = base
        """INSERT INTO Parametres VALUES(1, Normal, Journal)"""
        # definir les parametres par defaults ?

    def modifier_affichage (self, affichage):
        """permet de modifier l'affichage par default"""
        modification_affichage = """UPDATE Parametres SET Parametres_affichage = %s
        WHERE Parametre_ID = 1""" # pas sûre
        valeurs = affichage
        self.base.commit(modification_affichage, valeurs)

    def modifier_couleur (self, couleur):
        """permet de modifier la couleur par defaut"""
        modification_couleur = """UPDATE Parametres SET Parametres_couleur = %s
        WHERE Parametre_ID = 1""" # pas sûre
        valeurs = couleur
        self.base.commit(modification_couleur, valeurs)

    def get_tout(self):
        """permet de retourner tout les elements de parametres"""
        table_parametres = "SELECT * FROM Parametres WHERE Parametres_ID = 1"
        donnee = self.base.query(table_parametres)
        json_get_tout_parametres = json.dumps(donnee)
        return json_get_tout_parametres
