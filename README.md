# SU-LU3IN025-robots
UE LU3IN025 IA et Jeux, partie Robotique Autonome

# Pré-requis

Vous devez installer le simulateur [**Roborobo**](https://github.com/nekonaute/roborobo4/) sur votre machine avant de commencer. Ce simulateur s'installe facilement sous Linux et sous MacOS en suivant les [instructions](https://github.com/nekonaute/roborobo4/blob/main/README.md).

Remarques pour l'installation de _roborobo_ à la PPTI:
- vous devez configurer le proxy: _git config --global http.proxy http://proxy:3128_
- utilisez _conda_ (et pas _pip_)
- ne lancez pas les commandes _sudo apt(...)_ (les paquets sont déjà installés)
- utilisez _python3.7_, ou tout autre version strictement antérieure à la version 3.10
- lors de la commande _conda activate roborobo_, conda demande parfois de configurer le shell avec la commande _conda init_. Ignorer cette demande, et lancez un shell _tcsh_ (ie. tapez _tcsh_ à l'invite) puis la commande _conda activate roborobo_
- votre quota doit être suffisant pour installer et exécuter roborobo (env. 3.5go)

Si vous êtes sous Windows, ou si pour une raison ou une autre vous n'arrivez pas à installer Roborobo sur votre distribution Linux ou MacOS, nous vous suggérons d'installer le logiciel Virtualbox, et de créer une machine virtuelle Linux Ubuntu. 

# Instructions pour les TPs et le projet

Ce repository contient trois fichiers décrivant les sujets des deux TPs et le sujet de projet.

* [instructions_TP1.md](https://github.com/nekonaute/SU-LU3IN025-robots/blob/main/instructions_TP1.md): TP sur la conception de comportement. Braitenberg et architecture de subsomption. 
* [instructions_TP2.md](https://github.com/nekonaute/SU-LU3IN025-robots/blob/main/instructions_TP2.md): TP sur l'optimisation de comportement pour un robot autonome (recherche aléatoire, puis algorithmes génétiques).
* [instructions_projet.md](https://github.com/nekonaute/SU-LU3IN025-robots/blob/main/instructions_projet.md): description du projet.

Bon courage !
