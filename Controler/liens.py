"""liens entre front end et backend par les classes"""
from datetime import (datetime, date)
from Tables.Journal import Journal
from Tables.parametres import Parametres
from Tables.Tache import (Tache, SousTache)
from Tables.Tracker import Tracker
from base_de_donnee import Base

# tests journal :

mybase = Base()
journal1 = Journal(mybase, 'hello world', datetime.now(), 'hello hello world world', date.today())
print (journal1.get_tout)

journal1.get_tout()

#journal1.modifier("HELLO WORLD", date.today, 1)

# Tests Taches

# Tests Tracker

# Tests Parametres
