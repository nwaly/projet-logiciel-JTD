"""classe Calendrier"""

class Calendrier:
    """classe Calendrier (Calendrier_ID, Calendrier_jour)"""
    def __init__(self, base):
        self.base = base

    def creer_jour(self, date):
        """permet de crée un jour dans la table calendrier en entrant la date"""
        sql = """
        INSERT INTO calendrier (Calendrier_ID, Calendrier_jour) VALUES ((SELECT COALESCE(MAX(Calendrier_ID),0)+1), %s)
        """
        self.base.commit(sql, (date,))