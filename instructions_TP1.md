# TP 1 -  comportements réactifs

## Exercice 1: comportement de Braitenberg

Vous devez programmer des comportements de type Braitenberg. 

Comme vu dans les cours, il s'agit d'une méthode de programmation de comportement reposant sur des principes simples:
* les _effecteurs_ dépendent de la somme des activations des _senseurs_
* les connexions entre senseurs et effecteurs sont excitatrice (x1), inhibitrice (x-1) ou neutre (pas de connexion)
* comme vu dans le cours, un comportement de Braitenberg n'utilise **jamais** de structures conditionnelles (type if-then-else)

Pour cet exercice, les effecteurs sont au nombre de 2 (la vitesses de translation, et la vitesse de rotation) et les senseurs donnent la distance à l'obstacle, et détecte s'il s'agit d'un autre robot ou non.

En partant du code disponible dans le fichier comportement.py, vous devez programmer les comportements suivants:

* comportement "évite les obstacles (murs et robots)" (fichier _braitenberg_avoider.py_, à créer).
* comportement "va vers les murs et ignore les robots", (fichier _braitenberg_loveWall.py_, à créer)
* comportement "évite les murs et ignore les robots", (fichier _braitenberg_hateWall.py_, à créer)
* comportement "va vers les robots et ignore les murs" (fichier _braitenberg_loveBot.py_, à créer)
* comportement "évite les autres robots et ignore les murs" (fichier _braitenberg_hateBot.py_, à créer).

Remarque: "ignorer" signifie que l'objet est comme transparent (donc pas de connexion).

## Exercice 2: architecture de subsomption

Vous devez maintenant implémenter une architecture de Subsomption permettant à un robot de poursuivre les autres.

Définissez les règles d'activation et l'ordre de priorité entre comportements de type Braitenberg afin qu'un robot évite les murs et fonce sur un robot s'il en voit un.

Vous pouvez utiliser les comportements suivants:
* aller tout droit (nouveau comportement)
* éviter les murs (comportement _hatewall_)
* aller vers les robots (comportement _lovebot_)

Coder votre résultat dans un fichier _subsomption.py_ (en copiant le fichier _comportement.py_ pour commencer).
