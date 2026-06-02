# Rapprt du projet logiciel : Journal To-Do Tracker (version minimale)
## Déscription du projet : 
Le but de ce projet était de crée une application tournant en local qui permettait les fonctionnalités suivantes : 
### Journal : 
La fonctionnalité journal devait permettre de pouvoir :
- Ajouter une nouvelle entrée au journal (avec un titre et un contenu).
- Modifier le contenu d'une entrée déja ajoutée (en la séléctionnant pouvoir modifier son contenu).
- Visualiser les entrées ajoutées (leur titre, leur contenu, leur date de création).
### To-Do :
La fonctionnalité To-Do devrait perrmettre de pouvoir : 
- Ajouter une nouvelle tache (nom de la tache, date à laquelle elle doit être terminée).
- Modifier le statut d'une tâche (pour le faire passez de "non-faite" à "faite" (ou de "faite" à "non-faite")).
### Tracker : 
La fonctionnalité Tracker dervrait permettre de pouvoir : 
- Ajouter un nouveau Tracker (titre, déscription, icone, couleur).
- Appliquez un Tracker à un calendrier pour savoir quel jour quel objectif à été rempli.
## Technologies utilisées : 
Les technologies utilisées pour ce projet sont : 
- Visual Studio Code (comme éditeur de code).
- MySQL Workbench 8.0 CE (pour la création de la base de donnée et l'hébergement du serveur de la base).
- Flask (pour l'API, les liens entre la base et le front-end).
- GitHub (pour la collaboration sur le projet)
## Architecture du projet : 
Le projet est organisé en trois séctions principales : le Backend, le Controler et le Frontend. 
### Back-end : 
Le backend s'occupe de tout ce qui se passe en arrière plan, il conmprend : 
- La base de donnée, qui tourne sur un serveur MySQL.
- Le script de la base de donnée, qui se trouve dans la dossier "backend" du projet sous le nom de "base.sql".
### Controler : 
Le controler est l'entité qui fait le lien entre le back-end et le front-end, il comprend les fichiers :
- "__init__.py" qui sert à rendre le répertoire lisible par python.
- "base_de _donnee.py" qui instancie la classe "Base" qui possède les méthodes "display", "query" et "commit" qui permettent donner des requetes MySQL à la base. Le __init__ de "Base" permet aussi d'établir le lien avec la base de donnée.
Mais aussi deux répertoires "classe" et "flask" qui sont expliciter dans les deux séctions suivantes :
#### Les Classes
Les éléments du répertoire "classe" qui ce trouvent dans le repertoire "controler" sont des fichiers python qui définissent une classe pour chaque tableau de la base et qui spécifient les méthodes qui sont propres à chacunes de ces entités, le répertoire "classe" comprend : 
- "__init__.py" qui sert à rendre le répertoire lisible par python.
- ".Journal.py" qui définit la classe "Journal" ainsi que ces méthodes .
    - "nouveau" qui permet de crée une nouvelle entrée au journal et qui prend comme attribut le titre de l'entrée et son contenu.
    - "get_tout" qui permet de retourner tout les éléments du journal.
    - "modifier" qui permet de modifier le contenu d'une entrée et qui prend comme attribut le nouveau contenu de l'entrée ainsi que la date de la modification et l'id de l'entrée à modifiée.
    - "supprimer" qui permet de supprimer une entrée du journal.
- ".Tache.py" qui définit la classe "Tache" ainsi que ces méthodes.
    - "nouveau" qui permet de crée une nouvelle tache et qui prend comme attribut le nom de la tache, sa date buttoire d'execution, son statut et le fait qu'elle possède ou non une sous-tache (les sous-taches n'étant pas fonctionnelle dans cette version de l'application, cet attribut ne sert à rien, mais est déja implémenter dans le back-end, pour qu'il ne reste plus qu'à la crée dans le front-end).
    - "modification_statut" qui sert à valider ou invalider une tâche et qui prend comme attributs l'id de la tache à modifier ainsi que son nouveau statut
    - "modification_date" qui sert à modifier la date buttoire d'une tâche et qui prend comme attributs la date buttoire actuelle, le nom de la tache et sa nouvelle datte butoire.
    - "get_tout" qui permet de retourner toutes les taches.
    - "supprimer" qui permet de supprimer une tache.
    - ".Tache.py" contient aussi la classe "SousTache" qui n'est pas implémentée dans le front-end mais qui continue d'exister dans le back-end en vue d'une future implémentation.
- ".Tracker.py" qui définit la classe "Tracker" ainsi que ces méthodes :
    - "nouveau" qui permet de crée un nouveau tracker et qui prend comme attributs le nom du tracker, sa déscription, sa couleur et son icone.
    - "get_tout" qui permet de récuperer tout les trackers.
- ".calendrier.py" qui définit la classe "Calendrier" ainsi que sa méthode :
    - "creer_jour" qui permet de crée un jour et qui prend comme attribut la date du jour en question.
- "calendrier_has_tracker" qui définit la classe "CalendrierHasTracker" et ses méthodes : 
    - "trouve_tracker_par_jour" qui permet de récuperer tous les trackers pour un jour donné et qui prend comme attribut l'id du calendrier.
    - "activer_tracker" qui permet d'activer un tracker donné pour un jour donné et qui prend comme argument l'id du calendrier et l'id du tracker.
    - "desactiver_tracker" qui permet de desactiver un tracker donné pour un jour donné et qui prend comme argument l'id du calendrier et l'id du tracker.
- ".parametres.py" qui définit la classe "Parametres" et ses methodes :
    - "modifier_affichage" qui permet de modifier l'affichage par défaut et qui prend comme argument la nouvelle valeur de l'affichage .
    - "modifier_couleur" qui permet de modifier la couleur de l'affichage par défaut et qui prend comme argument la nouvelle valeur de la couleur.
    - "get_tout" qui permet de récuperer tout les éléments de Parametres.
#### Les Liens Flasks
Les éléments du répertoire "flask" qui ce trouvent dans le repertoire "controler" sont des fichiers python qui définissent les liens flask qui appelent les méthodes des classes et permettent ainsi de faire le lien entre l'interface utilisateur et la base de donnée. Les fichiers du répertoire "flask" se trouvant dans le répertoire "controler" sont les suivant :
- "__init__.py" qui sert à rendre le répertoire lisible par python.
- "journal_flask.py" qui instancie la classe Journal et crée les routes flasques suivantes :
    - "/journal" :
        - "POST" qui permet d'ajouter une entrée à journal en appelant "journal.nouveau".
        - "GET" qui permet de récuperer toutes les entrées de journal en appelant "journal.get_tout".
    - "/journal/<.int:id_>" :
        - "PUT" qui permet de modifier le contenu d'une entrée en appelant "journal.modifier" et qui prend l'id de l'entrée comme attribut.
        - "DELETE" qui permet de supprimer une entrée en appelant "journal.supprimer" et qui prend l'id de l'entrée comme attribut.
- "tache_flask.py" qui instancie la classe Tache et crée les routes flasques suivantes :
    - "/tache" :
        - "POST" qui permet d'ajouter une nouvelle tache en appelant "tache.nouveau".
        - "GET" qui permet de récuperer toutes les taches en appelant "tache.get_tout".
    - "/tache/<.int:id_>/statut" :
        - "PUT" qui permet de modifier le statut d'une tache en appelant "tache.modification_statut" et qui prend son id en argument.
        - "DELETE" qui permet de supprimer une tahce en appelant "tache.supprimer" et qui prend l'id de l'entrée comme attribut.
    - "/tache_date" : 
        - "PUT" qui permet de modifier la date buttoire d'une tache en appelant "tache.modification_tache" et qui prend comme attribut le nom, l'ancienne date et la nouvelle date butoire de la tache.
    - "tache_flask.py" instancie aussi et posède les liens pour la création et la récuperation de sous-taches qui ne sont pas implémentés dans la version actuelle de l'application.
- "tracker_flask.py" qui instancie les classe Tracker, Calendrier et CalendrierHasTracker et crée les routes flasques suivantes :
    - "/tracker" :
        - "POST" qui permet d'ajouter une un tracker en appelant "tracker.nouveau".
        - "GET" qui permet de récuperer toutes les entrées de tracker en appelant "tracker.get_tout".
    - "/calendrier" :
        - "POST" qui permet d'ajouter un nouveau jour à calendrier en appelant "calendrier.creer_jour".
    - "/calendrier/<.int:calendrier_id>/trackers" :
        - "GET" qui permet de récuperer tout les tracker d'un jour en appelant "calendrier_has_tracker.trouve_tracker_par_jour" et qui prends comme attributs l'id de calendrier.
    - "/calendrier/<.int:calendrier_id>/tracker/<.int:tracker_id>/activer_desactiver :
        - "POST" qui permet de désactiver ou d'activer un tracker pour un jour donné en appelant soit "calendrier_has_tracker.activer_tracker" soit "calendrier_has_tracker.desactiver_tracker" et en prenant comme attributs l'id du calendrier et l'id du tracker.
- "parametre_flask.py" qui instancie la classe Parametres et crée les routes flasques suivantes :
    - "/parametre"
        - "GET" permet de récuperer toutes les données de parametres en appelant "parametre.get_tout".
    - "/parametre_statut" 
        - "PUT" permet de modifier le statut des parametres.
    - "/parametre_couleur" 
        - "PUT" permet de modifier les couleur des parametres.
### Front-End : 
!!!!!!!!!!!!!!!!!


## Organisation du projet : 
Le projet a été réalisé du 04.03.26 au 03.05.26. 
### Répartition des tâches : 
![image de la gantt chart](../images/Gantt_chart.png "Gantt_chart pour cette version du projet")
## Fonctionnement du logiciel :
!!!!!!!!!!!!!!!
### Page Journal :
!!!!!!!!!!!!!!!
![image de la page Journal](../images/Journal.png "Page Journal")
### Page Tache : 
!!!!!!!!!!!!!!!!
![image de la page ToDo](../images/ToDo.png "Page ToDo")
### Page Tracker : 
!!!!!!!!!!!!!!!!!!!!!
![image de la page Tracker](../images/Tracker.png "Page Tracker") 
### Page Paramètres : 
!!!!!!!!!!!!!!!!!!!!!
![image de la page Settings](../images/Settings.png "Page Settings")

