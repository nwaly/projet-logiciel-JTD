"""Table Tache"""

class Tache :
    """classe table (Tache_ID, Tache_date, Tache_nom, Tache_statut, Tache_sous_tache)"""
    def __init__(self, base):

        self.base = base
    def nouveau(self, nom, date, statut, sous_tache):
        """permet de cree une nouvelle tache"""
        tache = """INSERT INTO Tache (Tache_nom, Tache_date, Tache_statut, Tache_sous_tache)
        VALUES (%s, %s, %s, %s)"""
        valeurs = (nom, date, statut, sous_tache)
        self.base.commit(tache, valeurs)


    def modification_statut(self, nom ,date, statut):
        """permet de valider une tache"""
        def get_statut_id(date, nom):
            """retourne l'id de la tache à chercher"""
            get_id = """SELECT Tache_ID FROM Tache WHERE Tache_date= %s AND Tache_nom = %s"""
            valeurs = (date, nom)
            id_resultat = self.base.query(get_id, valeurs)
            if id_resultat and len(id_resultat)>0:
                return id_resultat[0]
            return None
        id_statut = get_statut_id(date, nom)
        tache_validation = """UPDATE Tache SET Tache_statut = %s
        WHERE Tache_ID = %s"""
        valeurs = (statut, id_statut)
        self.base.commit(tache_validation, valeurs)

    def modification_date(self, date, nom, date_modification,):
        """permet de reporter la validation d'une tache"""
        def get_statut_id(nom, date):
            """retourne l'id de la tache à chercher"""
            get_id = """SELECT Tache_ID FROM Tache WHERE Tache_date= %s AND Tache_nom = %s"""
            valeurs = (date, nom)
            id_resultat = self.base.query(get_id, valeurs)
            if id_resultat and len(id_resultat)>0:
                return id_resultat[0]
            return None
        id_date = get_statut_id(nom, date)
        tache_deplacement = """UPDATE Tache SET Tache_date = %s
        WHERE Tache_ID = %s"""
        valeurs = (date_modification, id_date)
        self.base.commit(tache_deplacement, valeurs)

    def get_tout(self):
        """permet de retourner tout les elements de tache ordonnés selon leur date de 
        validation effective ou presumée"""
        table_tache = "SELECT * FROM Tache ORDER BY Tache_date"
        return self.base.query(table_tache)

class SousTache :#     """Classe Sous_Tache (Sous_Tache_ID, Sous_Tache_nom, Sous_Tache_statut, Tache_Tache_ID)"""
     def __init__(self, base):
         self.base = base
     def nouveau(self, nom, statut, tache_id):
         """permet de cree une nouvelle sous-tache"""
         sous_tache = """INSERT INTO Sous_Tache (Sous_Tache_nom, Sous_Tache_statut, Tache_Tache_ID)
         VALUES (%s, %s, %s)"""
         valeurs = (nom, statut, tache_id)
         self.base.commit(sous_tache, valeurs)

#     def get_tout(self):
#         """permet de retourner tout les elements de sous-tache ordonnés selon l'id de la tache
#         à laquelle elle sont liées"""
#         table_sous_tache = "SELECT * FROM Sous_Tache ORDER BY Sous_Tache_ID"
#         return self.base.query(table_sous_tache)
