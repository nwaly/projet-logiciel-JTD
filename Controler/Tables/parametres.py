"""Table Parametres"""

class Parametres :
    """classe Parametres : Parametres_ID, Parametres_affichage, Parametres_couleur"""
    def __init__(self, base):
        self.base = base
        # definir les parametres par defaults ?

    def modifier_affichage (self, affichage):
        """permet de modifier l'affichage par default"""
        modification_affichage = """UPDATE Parametres SET Parametres_affichage ='affichage'
        WHERE Parametre_ID = 1""" # pas sûre
        self.base.execute(modification_affichage)

    def modifier_couleur (self, couleur):
        """permet de modifier la couleur par defaut"""
        modification_couleur = """UPDATE Parametres SET Parametres_couleur ='couleur'
        WHERE Parametre_ID = 1""" # pas sûre
        self.base.execute(modification_couleur)

    def get_tout(self):
        """permet de retourner tout les elements de parametres"""
        table_parametres = "SELECT * FROM Parametres WHERE Parametres_ID = 1"
        return self.base.query(table_parametres)
