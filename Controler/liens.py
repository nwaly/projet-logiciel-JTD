"""liens entre front end et backend par les classes"""
from datetime import (date)
from Tables.Journal import Journal
from Tables.parametres import Parametres
from Tables.Tache import (Tache, SousTache)
from Tables.Tracker import Tracker
from base_de_donnee import Base

# tests journal :

mybase = Base()
journal1 = Journal(mybase, 'hello world', 'hello hello world world')
print (journal1.get_tout())
#journal1.modifier("HELLO WORLD", date.today(), 1)

# Tests Taches
#tache1 = Tache(mybase, "manger", "2027-05-13", 0, 0)
#print(tache1.get_tout())
#tache1.modification_statut("manger", "2027-05-13", 1)
#print(tache1.get_tout())
#tache1.modification_date("2027-05-13", "manger", "2030-10-22")
#print(tache1.get_tout())

# Tests Tracker

tracker1 = Tracker(mybase, "eau", "boire 1 litre d'eau chaque jour", "rouge", "rond")
print(tracker1.get_tout())

# Tests Parametres
