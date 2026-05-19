"""Table Tracker"""

class Tracker ():
    """classe tracker (Tracker_ID, Tracker_nom, Tracker_description, 
    Tracker_couleur, Tracker_icone)"""
    def __init__(self, base):
        self.base = base
    def nouveau(self, nom, description, couleur, icone):
        """permet de cree un nouveau tracker"""
        sql = """INSERT INTO Tracker (Tracker_ID, Tracker_nom, Tracker_description,
        Tracker_couleur, Tracker_icone)
        VALUES (SELECT COALESCE(MAX(Tracker_ID),0)+1, %s, %s, %s, %s)"""
        valeurs = (nom, description, couleur, icone)
        self.base.commit(sql, valeurs)

    def get_tout(self):
        """permet de retourner tout les elements du Tracker ordonner selon leur id"""
        table_tracker = "SELECT * FROM Tracker ORDER BY Tracker_ID"
        return self.base.query(table_tracker)
