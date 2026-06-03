"""classe CalendrierHasTracker"""

class CalendrierHasTracker:
    """classe CalendrierHasTracker (Calendrier_has_tracker_Calendrier_ID, Calendrier_has_tracker_Tracker_ID Calendrier_has_Tracker_Statut)"""
    def __init__(self, base):
        self.base = base

    def trouve_tracker_par_jour(self, calendrier_id):
        """permet de récuperer tout les tracker pour un jour donner"""
        sql = """
        SELECT tracker.Tracker_ID, tracker.Tracker_nom, tracker.Tracker_description, tracker.Tracker_couleur, tracker.Tracker_icone, calendrier_has_tracker.Calendrier_has_Tracker_Statut 
        FROM calendrier_has_tracker JOIN tracker
        ON tracker.Tracker_ID = calendrier_has_tracker.Tracker_Tracker_ID
        WHERE calendrier_has_tracker.Calendrier_Calendrier_ID = %s
        ORDER BY tracker.Tracker_ID;
        """
        return self.base.query(sql, (calendrier_id,))

    def activer_tracker(self, calendrier_id, tracker_id):
        """permet d'activer un tracker donné pour un jour donné"""
        sql = """
        INSERT INTO calendrier_has_tracker (Calendrier_Calendrier_ID, Tracker_Tracker_ID, Calendrier_has_Tracker_Statut)
        VALUES (%s, %s, 1) ON DUPLICATE KEY UPDATE Calendrier_has_Tracker_Statut = 1
        """
        self.base.commit(sql, (calendrier_id, tracker_id))

    def desactiver_tracker(self, calendrier_id, tracker_id):
        """permet de desactiver un tracker donné pour un jour donné"""
        sql = """
        UPDATE calendrier_has_tracker SET Calendrier_has_Tracker_Statut = 0 
        WHERE Calendrier_Calendrier_ID = %s AND Tracker_Tracker_ID = %s
        """
        self.base.commit(sql, (calendrier_id, tracker_id))
