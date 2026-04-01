"""liens entre front end et backend par les classes"""
from datetime import (datetime, date)
from Tables.journal import Journal
from Tables.parametres import Parametres
from Tables.tache import (Tache, SousTache)
from Tables.tracker import Tracker
from base_de_donnee import Base 

# testes journal :


journal1 = Journal("mydb", "hello world", datetime.now(), "hello hello world world", date.today())
print (Journal.get_tout)
