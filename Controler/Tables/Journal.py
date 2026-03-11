"""Controler Journal"""

class Journal:
    """classe Journal : ID, titre, date, heure, contenu, modification(date)"""
    def __init__(self, base):
        self.base = base


    def nouvelle_entree(self, titre, date, contenu, modification):
        """permet de cree une nouvelle entrée"""
        sql = """INSERT INTO Journal (Journal_date, Journal_heure, Journal_contenu, Journal_modification, Journal_titre)
        VALUES ( "journal_titre", "journal_date", "journal_contenu", "journal_modification")"""
        self.base.execute(sql, (titre, date, contenu, modification, ))

    def get_tout(self):
        """permet de retourner tout les elements du journal ordonner selon leur date"""
        table_journal = "SELECT * FROM Journal ORDER BY Journal_Date"
        return self.base.query(table_journal)

    
    def modifier(self, contenu, modification, journal_id):
        """permet de modifier le contenu d'un texte et change aussi la dernière 
        date de modification"""
        modification_contenu = "UPDATE Journal SET Journal_contenu ='contenu' WHERE Journal_ID = 'journal_id'" # pas sûre
        modification_modification = "UPDATE Journal Journal_modification ='modification' WHERE Journal_ID = 'journal_id'" # pas sûre
        self.base.execute(modification_contenu, modification_modification)       