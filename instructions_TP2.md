# TP 2 - optimisation de comportements

## Exercice 1: recherche aléatoire 

Etudiez la fonction _step_ du fichier _optimisation.py_. 

Cette fonction montre comment faire une recherche aléatoire dans l'espace des paramètres d'un réseau de neurones artificiels simple (un Perceptron sans couche cachée utilisant une fonction d'activation tangente hyperbolique).

On considère que chaque paramètre peut prendre la valeur -1 (inhibition), +1 (excitation) ou 0 (pas de connexion).

Le score d'un individu dépend de la distance euclidienne parcourue en 400 itérations depuis la position initiale au centre de l'écran.

Créez le fichier _randomsearch.py_ (en copiant _optimisation.py_), puis modifiez le comme suit:
* utilisez la variable _evaluations_ déjà créée pour fixer le nombre de comportements générés aléatoirement et évalués.
* à chaque fois qu'un comportement est meilleur que les précédents, sauvegardez-le (score, valeur des paramètres et _itération_ ou il a été créé).
* après avoir épuisé le budget d'évaluations, rejouez le meilleur comportement trouvé pendant _1000_ itérations, puis recommencez (i.e. le meilleur comportement est réévalué à l'infini).

Remarques:
* la variable _simulation_mode_ permet de régler la vitesse de la simulation au démarrage. Pratique pour faire une recherche rapide (valeur 1, voire 2).
* pendant la simulation, la touche _d_ permet de changer la vitesse de simulation. Pratique pour observer le meilleur comportement à vitesse normale.
* n'oubliez pas de sauvegarder votre meilleur individu quelque part (p.ex. en affichant ses paramètres dans le terminal)

## Exercice 2: effet des conditions initiales

Un inconvénient du programme précédent vient du fait que la condition initiale (position et orientation initiale) est toujours la même. Cela ne permet pas de garantir que le comportement obtenu sera efficace dans une autre situation. 

En partant du programme précédent (créez un fichier _randomsearch2.py_), modifier le code afin que chaque comportement soit évalué _3_ fois, en tirant aléatoirement l'orientation initiale à chaque fois. Le score d'un comportement sera la somme de ces 3 évaluations.

Remarque: 
* vous pouvez aussi, si vous le souhaitez, faire varier la position de départ (éviter de positionner votre robot dans un mur quand même).

## Exercice 3: algorithme génétique

Créez le fichier _genetic_algorithms.py_ (en copiant le précédent) et implémentez un algorithme génétique à la place de la recherche aléatoire, comme vu en cours:
* opérateur de sélection: _( mu=1 + lambda=1 )_
* opérateur de mutation: sélection d'un paramètre au hasard, et remplacement de sa valeur au hasard sans retirage (c'est à dire que la nouvelle valeur est forcément différente de la précédente)

C'est à dire qu'à chaque génération un seul enfant est créé à partir du parent en modifiant la valeur d'un seul paramètre. Si l'enfant est meilleur que le parent, alors il remplace le parent. Sinon, le parent est conservé (et l'enfant effacé).  

Pour un nombre d'_itérations_ identique, comparez les résultats obtenus par la recherche aléatoire et la recherche par algorithme génétique. Pour chaque méthode, vous tracerez un graphe compilant les résultats de 10 essais indépendants.

## Exercice 4: affichage et comparaison des résultats 

Modifiez les codes que vous venez d'écrire pour les questions 2 et 3 afin de sauvegarder dans un fichier les informations suivantes pour chaque évaluation:
* numéro de l'itération à partir duquel le comportement actuel est testé 
* score du comportement actuel
* meilleur score obtenu depuis le début
* valeurs des meilleurs paramètres

Cela donnera par exemple (si chaque comportement est testé pendant 400 itérations):
* 0, 225.3660952, 225.3660952
* 400, 199.618627164, 225.3660952
* 800, 80.8005718674, 225.3660952
* 1200, 642.2593266, 642.2593266 
* _etc._

Dans le répertoire _multiplotCSV_, vous trouverez un script permettant de tracer un graphique (consultez le fichier _aide.txt_). Utilisez-le pour:
* tracer le résultat d'une recherche (axe X: evaluations, axe Y: score), en traçant pour chaque itération le meilleur individu trouvé jusqu'ici. (cf. premier exemple du fichier _aide.txt_)
* tracer la performance moyenne d'une recherche aléatoire en compilant 10 essais indépendants. (cf. second exemple du fichier _aide.txt_)

Remarques:
* Plutôt que de sauvegarder directement les informations demandées dans un fichier, vous pouvez aussi les afficher dans le terminal, et les copier manuellement dans un fichier.

## Quelques idées pour le projet

* implémentez une fonction score qui favorise les robots se déplaçant rapidement sans tourner (cf. cours). C'est à dire tel que
  * score = somme_sur_toutes_les_iterations ( vitesse_de_translation * ( 1 - abs(vitesse_de_rotation) ) ) 
* implémentez une fonction score calculant la couverture de l'environnement, par exemple en le découpant en cases (cf. projet)
* implémentez un opérateur de sélection (mu=5,lambda=20)
* modifiez l'opérateur de mutation afin d'explorer un taux de mutation plus élevé

L'algorithme génétique peut vous permettre de trouver une solution exploitable pour votre projet, à condition de bien définir la fonction score (pour guider la recherche) et les conditions d'expérience (pour garantir l'aspect générique de la solution).
