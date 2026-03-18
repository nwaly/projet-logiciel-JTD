"""lien avec la base de donnee"""
import mysql.connector

class Base :
    """classe base de donnee"""
    def __init__(self):
        self.connexion = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "Fuji06Maxoue09",
            database = "mydb",
            port = 3306,
        )

        self.curseur = self.connexion.cursor(dictionary=True)

    def display(self):
        """montre la connection de la base"""
        print(self.connexion)

    def query (self, sql):
        """retourne toute les lignes de sql"""
        self.curseur.execute(sql)
        return self.curseur.fetchall()

    def commit (self, sql):
        """permet de commit la requête"""
        self.curseur.execute(sql)
        self.connexion.commit()
