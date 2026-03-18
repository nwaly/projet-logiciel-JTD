"""table Tracker"""

class Tracker ():
    """classe tracker (Tracker_ID, Tracker_nom, Tracker_description, 
    Tracker_couleur, Tracker_icone)"""
    def __init__(self, base):
        self.base = base

    def nouveau_tracker(self, nom, description, couleur, icone):
        """permet de cree un nouveau tracker"""
        sql = """INSERT INTO Journal (Tracker_nom, Tracker_description,
        Tracker_couleur, Tracker_icone)
        VALUES ( "nom", "description", "couleur", "icone")"""
        self.base.execute(sql, (nom, description, couleur, icone))

    def get_tout(self):
        """permet de retourner tout les elements du Tracker ordonner selon leur id"""
        table_tracker = "SELECT * FROM Tracker ORDER BY Tracker_ID"
        return self.base.query(table_tracker)

    # comment relier ça avec calendrier ?
