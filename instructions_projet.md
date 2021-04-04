# Projet - "paint wars"

## Description

Deux équipes de 8 robots ("red team" et "blue team") s'affrontent pour visiter au mieux un arène découpée en case. Chaque case appartient à l'équipe qui l'a visitée en dernier. Le temps est limité. L'équipe ayant visité le plus de cases après 2000 itérations gagne.

Executez le fichier _paintwars.py_ pour avoir un aperçu du projet. 

Tout les coups sont permis, tant que votre code tient exlusivement dans la fonction _step_ du fichier _paintwars_team_challenger_ dans la fonction step (pas de mémoire, pas d'information supplémentaire que celles données par les senseurs, etc.). Pour commencer, n'hésitez pas à réutiliser les comportements déjà obtenus dans les TP1 et TP2.

## Fichiers

Fichiers importants, à modifier:
* _paintwars_team_challenger.py_: votre stratégie.
  * get_team_name(): renvoi le nom de votre équipe (à vous de décider)
  * def step(robotId, sensors): 
    * en entrée: numéro du robot et information sensorielle
    * en sortie: renvoie vitesse de translation et vitesse de rotation
  * remarque: vous pouvez renommer ce fichier (il faudra mettre _paintwars_config.py_ à jour).
* _paintwars_config.py_: 
  * _arenaIndexSelector_: numéro du labyrinthe utilisé (entre 0 et 4)
  * _invertStartingPosition_: inverse les positions de départ des deux équipes
  * _step_red_team_ et _get_name_red_team_: alias vers les fonctions que vous aurez défini dans _paintwars_team_challenger.py_
  
Autres fichiers, à ne pas modifier.

* _paintwars.py_: le programme principal. _Ne pas modifier._ 
* _paintwars_team_champion.py_: le comportement fourni par défaut, contre lequel il va falloir faire du mieux possible! _Ne pas modifier._
* _paintwars_arena.py_: défini les arènes possibles. Sélectionnable via la variable _arenaIndexSelector_ dans _paintwars_config.py_. Vous pouvez éventuellement _ajouter_ des cartes pour faire des tests, mais vous ne pouvez _pas_ modifier les cartes existantes (ni leur numéro).

## Evaluation

Lors de la dernière séance de TP, vous présenterez votre travail pendant une interview de 15 minutes environ, en faisant tourner votre code sur écran partagé.

Vous devrez présenter:
* les résultats de votre stratégie préférée contre l'équipe _paintwars_team_champion_. Pour chacun des 5 labyrinthes, vous devrez faire deux essais (équipe rouge démarrant à gauche, puis à droite).
* même chose, mais sur 5 nouveaux labyrinthes inédits
* expliquer votre architecture à l'oral, c'est à dire l'architecture globale et les comportements de base. Vous _devez_ avoir au moins un comportement de base obtenu par algorithme génétique. 
* répondre aux questions qui pourront porter sur les méthodes utilisées ou sur le code.

De plus, vous devrez vous coordonner avec les autres groupes de votre séance pour faire un tournoi. Chaque groupe devra rencontrer le maximum de groupes adversaires, sur les 10 labyrinthes (2 matches par labyrinthe, en variant la position de départ). Pour cela, vous modifierez _paintwars_config.py_ pour faire s'affronter les deux équipes. 

Vous reporterez les résultats du tournoi sur un document partagé prévu à cet effet.

Le dernier push de votre projet avant le début de la séance d'évaluation sera pris en compte.
