# TP 1 -  comportements réactifs

## Exercice 1: comportement de Braitenberg

Vous devez programmer des comportements de type Braitenberg. 

Comme vu dans les cours, il s'agit d'une méthode de programmation de comportement reposant sur des principes simples:
* les _effecteurs_ dépendent de la somme des activations des _senseurs_
* une connexion entre unsenseur et un effecteur peut être soit excitatrice, inhibitrice ou absente
* comme vu dans le cours, un comportement de Braitenberg n'utilise **jamais** de structures conditionnelles (type if-then-else)

Pour cet exercice, les effecteurs sont au nombre de 2 (la vitesses de translation, et la vitesse de rotation) et les senseurs donnent la distance au mur ou au robot le plus proche (1.0 si absent). Cf. exemple dans le code.

En partant du code disponible dans le fichier comportement (que vous copierez), vous devez programmer les comportements suivants en modifiant uniquement la fonction _step_ en début de fichier. Seules les deux lignes marquées "_A MODIFIER_" doivent être changées.

* comportement "évite les obstacles (murs et robots)" (fichier _braitenberg_avoider.py_, à créer).
* comportement "va vers les murs et ignore les robots", (fichier _braitenberg_loveWall.py_, à créer)
* comportement "évite les murs et ignore les robots", (fichier _braitenberg_hateWall.py_, à créer)
* comportement "va vers les robots et ignore les murs" (fichier _braitenberg_loveBot.py_, à créer)
* comportement "évite les autres robots et ignore les murs" (fichier _braitenberg_hateBot.py_, à créer).

Remarques: 
* "ignorer" signifie que l'objet est comme transparent (donc pas de connexion).
* même si ce n'est pas obligatoire, il est possible de répondre à l'ensemble des questions en utilisant uniquement les senseurs _sensor_front_, _sensor_front_right_ et _sensor_front_left_

## Exercice 2: architecture de subsomption

Vous devez maintenant implémenter une architecture de Subsomption permettant à un robot de poursuivre les autres.

Définissez les règles d'activation et l'ordre de priorité entre comportements de type Braitenberg afin qu'un robot évite les murs et fonce sur un robot s'il en voit un. Vous ne modifierez que la fonction _step_ en début du fichier, mais vous pouvez rajouter d'autres fonctions si vous le souhaitez (par exemple pour chaque comportement de Braitenberg que vous allez utiliser).

Vous pouvez utiliser les comportements suivants:
* aller tout droit (nouveau comportement)
* éviter les murs (comportement _hatewall_)
* aller vers les robots (comportement _lovebot_)

Coder votre résultat dans un fichier _subsomption.py_ (en copiant le fichier _comportement.py_ pour commencer).

Remarques:
* si tous vos robots suivent ce nouveau comportement, on s'attend à ce que les robots forment des aggrégats (puisqu'ils vont rentrer en collision).
* vous pouvez tester un comportement de suivi en n'exécutant ce comportement que sur un robot. Pour cela, il est possible d'utiliser la variable _robotId_ disponible dans la fonction _step_ qui donne le numéro d'identifiant du robot. Vous pouvez par exemple décider que seul le robot no.0 utilise l'architecture de subsomption, alors que tous les autres utilisent le comportement d'évitement d'obstacle codé dans l'exercice précédent.

## Quelques idées pour le projet

Utiliser une architecture de subsomption (ou un arbre de comportement) est un bon moyen d'organiser vos différents comportements de base. Cela permet aussi de se concentrer sur la conception de comportements spécialisés (i.e. des comportements peu complexes mais efficace dans un contexte particulier). En combinant ainsi des comportements spécialisés, on peut obtenir des stratégies capables de réagir efficacement dans des contextes différents.
