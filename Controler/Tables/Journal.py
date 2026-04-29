"""Controler Journal"""
import json
from pathlib import Path

class Journal :
    """classe Journal : ID, titre, date, contenu, modification"""
    def __init__(self, base, titre, contenu):
        self.base = base
        """permet de cree une nouvelle entrée"""
        sql = """INSERT INTO Journal (Journal_titre, Journal_contenu)
        VALUES (%s, %s)"""
        valeurs = (titre, contenu)
        self.base.commit(sql, valeurs)

    def get_tout(self):
        """permet de retourner tout les elements du journal ordonner selon leur date"""
        get_tout_journal = Path("get_tout_journal.json")
        table_journal = "SELECT * FROM Journal ORDER BY Journal_date"
        donnee =self.base.query(table_journal)
        with open(get_tout_journal, 'w', encoding='utf-8') as file:
            json.dump(donnee, file)


    def modifier(self, contenu, modification, id_):
        """permet de modifier le contenu d'un texte et change aussi la dernière 
        date de modification"""
        modifier_contenu = """ UPDATE Journal SET Journal_contenu = %s,
        journal_modification = %s WHERE Journal_ID = %s
         """
        valeurs = (contenu, modification, id_)
        self.base.commit(modifier_contenu , valeurs)
