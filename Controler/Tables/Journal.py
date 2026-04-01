"""Controler Journal"""

class Journal:
    """classe Journal : ID, titre, date, contenu, modification"""
    def __init__(self, base, titre, date_, contenu, modification):
        Journal.base = base
        """permet de cree une nouvelle entrée"""
        sql = f"""INSERT INTO Journal (Journal_titre, Journal_date, Journal_contenu,
        Journal_modification)
        VALUES ({titre},{date_},{contenu},{modification})"""
        self.base.execute(sql, (titre, date_, contenu, modification))

    def get_tout(self):
        """permet de retourner tout les elements du journal ordonner selon leur date"""
        table_journal = "SELECT * FROM Journal ORDER BY Journal_date"
        return self.base.query(table_journal)

    def modifier(self, contenu, modification, id_):
        """permet de modifier le contenu d'un texte et change aussi la dernière 
        date de modification"""
        modification_contenu = f"""UPDATE Journal SET Journal_contenu = {contenu}
        WHERE Journal_ID = {id_}"""
        modification_modification = f"""UPDATE Journal Journal_modification = {modification}
        WHERE Journal_ID = {id_}"""
        self.base.execute(modification_contenu, modification_modification)

        # json
