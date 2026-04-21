"""lien avec la base de donnee"""
import mysql.connector

class Base:
    """classe base de donnee"""
    def __init__(self):
        self.connexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Fuji06Maxoue09",
            database="mydb",
            port=3306,
        )

        self.curseur = self.connexion.cursor(dictionary=True)

    def display(self):
        """montre la connection de la base"""
        print(self.connexion)

    def query(self, requete_sql, valeurs=None):
        """retourne toutes les lignes de sql, avec support des paramètres"""
        if valeurs:
            self.curseur.execute(requete_sql, valeurs)
        else:
            self.curseur.execute(requete_sql)
        return self.curseur.fetchall()

    def commit(self, requete_sql, valeurs=None):
        """permet de commit la requête, avec support des paramètres"""
        if valeurs:
            self.curseur.execute(requete_sql, valeurs)
        else:
            self.curseur.execute(requete_sql)
        self.connexion.commit()


