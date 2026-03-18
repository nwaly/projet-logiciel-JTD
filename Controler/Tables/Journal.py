"""Controler Journal"""

class Journal:
    """classe Journal : ID, titre, date, contenu, modification(date)"""
    def __init__(self, base):
        self.base = base

    def nouvelle_entree(self, titre, date, contenu, modification):
        """permet de cree une nouvelle entrée"""
        sql = """INSERT INTO Journal (Journal_date, Journal_contenu,
        Journal_modification, Journal_titre)
        VALUES ( "titre", "date", "contenu", "modification")"""
        self.base.execute(sql, (titre, date, contenu, modification, ))

    def get_tout(self):
        """permet de retourner tout les elements du journal ordonner selon leur date"""
        table_journal = "SELECT * FROM Journal ORDER BY Journal_date"
        return self.base.query(table_journal)

    def modifier(self, contenu, modification, id):
        """permet de modifier le contenu d'un texte et change aussi la dernière 
        date de modification"""
        modification_contenu = """UPDATE Journal SET Journal_contenu = 'contenu'
        WHERE Journal_ID = 'id'""" # pas sûre
        modification_modification = """UPDATE Journal Journal_modification = 'modification'
        WHERE Journal_ID = 'id'""" # pas sûre
        self.base.execute(modification_contenu, modification_modification)
