# Projet - Paint Wars

## Description

Deux équipes de 8 robots ("red team" et "blue team") s'affrontent pour visiter au mieux une arène découpée en cases. Une case appartient à l'équipe qui l'a visitée en dernier. Le temps est limité et l'équipe qui possède le plus de cases après 2000 itérations gagne. Il s'agit là d'une variation compétitive du _problème de la patrouille multi-agents_, un problème classique en robotique.

Executez le fichier _paintwars.py_ pour avoir un aperçu du projet.

Pour commencer, n'hésitez pas à réutiliser les comportements déjà obtenus dans les TP1 et TP2. Dans votre architecture de comportement finale, il est demandé d'avoir _au moins_ un comportement type Braitenberg _et_ un comportement obtenu précédemment par algorithme génétique.

Tout les coups sont permis, tant que votre code tient exlusivement dans la fonction _step_ du fichier _paintwars_team_challenger_ (pas de mémoire, pas de communication, pas d'information supplémentaire que celles données par les senseurs, etc.).

## Fichiers

Fichiers importants, à modifier:
* _paintwars_team_challenger.py_: votre stratégie comportementale.
  * get_team_name(): renvoie le nom de votre équipe (à vous de décider son nom)
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
* _paintwars_arena.py_: défini les arènes possibles. Sélectionnable via la variable _arenaIndexSelector_ dans _paintwars_config.py_. Vous pouvez éventuellement _ajouter_ des cartes pour faire des tests si vous le souhaitez.

Vous pouvez aussi utiliser le script _go_tournament_ qui permet de lancer 10 matches (2 matches par arène, en changeant la position de départ -- l'équipe rouge démarrera à gauche, puis à droite).

_paintwars.py_ utilise par défaut les paramètres spécifiés dans _paintwars_config.py_ (numéro d'arène, position de départ, vitesse de rendu). Cependant, il est possible de lancer _paintwars.py_ avec des paramètres en ligne de commande, comme suit:

* _python paintwars.py <numero_arene> <inverser_position_de_depart> <vitesse_de_simulation>_
** <numero_arene> : entre 0 et 5
** <inverser_position_de_depart> : False ou True
** <vitesse_de_simulation> : 0 (normal), 1 (rapide), 2 (très rapide, pas d'affichage)
** Exemple: _python paintwars.py 3 True 1_

## Evaluation

Lors de la dernière séance de TP, vous présenterez votre travail pendant une interview de 15 minutes environ, en faisant tourner votre code.

Nous vous fournirons au début de la séance deux nouveaux fichiers:
1. _go_tournament_eval_ qui permet de lancer un tournoi sur l'ensemble des arènes initialement fournies, ainsi que de nouvelles arènes
2. _paintwars_arena_grX.py_ qui définit de nouvelles arènes inédites. le _X_ correspond à votre numéro de groupe.

Pour utiliser ces nouvelles arènes, vous devez modifier le fichier _paintwars_config.py_ (ligne 4) en remplaçant _paintwars_arena.py_ par le fichier fourni _paintwars_arena_grX.py_.

On vous demandera de:
* utiliser le script _go_tournament_final_ pour présenter les scores de votre stratégie préférée contre l'équipe _paintwars_team_champion_ pour chacun des 5 labyrinthes initiaux ainsi que les 5 labyrinthes inédits;
* utiliser _paintwars.py_ pour faire une démonstration des stratégies que vous avez implémentés;
* expliquer votre architecture à l'oral, c'est à dire l'architecture globale et les comportements de base. ;
* répondre aux questions qui pourront porter sur le code et sur les méthodes utilisées ou vues en cours.

Pendant la séance (hors interview), vous devrez vous coordonner avec les autres groupes de votre séance pour faire un tournoi. Chaque groupe devra rencontrer le maximum de groupes adversaires, sur les 10 labyrinthes (2 matches par labyrinthe, en variant la position de départ). Pour cela, vous utiliserez le script _go_tournament_ modifierez _paintwars_config.py_ pour faire s'affronter les deux équipes (i.e. une équipe jouera les bleus).

Vous reporterez les résultats du tournoi sur un document partagé prévu à cet effet.

Le dernier _git push_ de votre projet avant le début de la séance d'évaluation sera pris en compte comme rendu.
