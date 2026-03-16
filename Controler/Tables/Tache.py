"""Table Tache"""
class Tache :
    """classe table (Tache_ID, Tache_date, Tache_nom, Tache_statut, Tache_sous_tache)"""
    def __init__(self, base):
        self.base = base

    def nouvelle_tache(self, nom, date, statut, sous_tache):
        """permet de cree une nouvelle tache"""
        tache = """INSERT INTO Tache (Tache_nom, Tache_date, Tache_statut, Tache_sous_tache)
        VALUES ('nom', 'date', 'statut','sous_tache')"""
        self.base.execute(tache, (nom, date, statut, sous_tache ))

    def modification_statut(self, statut):
        """permet de valider une tache"""
        tache_validation = """UPDATE Tache SET Tache_statut = 'statut'
        WHERE Tache_ID = 'id'"""
        self.base.execute(tache_validation)

    def modification_date(self, date):
        """permet de reporter la validation d'une tache"""
        tache_deplacement = """UPDATE Tache SET Tache_date = 'date'
        WHERE Tache_ID = 'id'"""
        self.base.execute(tache_deplacement)

class SousTache :
    """Classe Sous_Tache (Sous_Tache_ID, Sous_Tache_nom, Sous_Tache_statut, Tache_Tache_ID)"""
    def __init__(self, base):
        self.base = base

    def nouvelle_sous_tache(self, nom, statut, tache_id):
        """permet de cree une nouvelle sous-tache"""
        sous_tache = """INSERT INTO Sous_Tache (Sous_Tache_nom, Sous_Tache_statut, Tache_Tache_ID)
        VALUES ('nom', 'statut','tache_id')"""
        self.base.execute(sous_tache, (nom, statut, tache_id))
