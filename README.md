# SU-LU3IN025-robots
UE LU3IN025 IA et Jeux, partie Robotique Autonome

# Pré-requis

Vous devez installer le simulateur [**Roborobo**](https://github.com/nekonaute/roborobo4/) sur votre machine avant de commencer. Ce simulateur s'installe facilement sous Linux et sous MacOS en suivant les [instructions](https://github.com/nekonaute/roborobo4/blob/main/README.md). Si vous souhaitez l'utiliser sous Windows, il est suggéré d'utiliser une machine virtuelle (éventuellement fourni par le/la chargé/e de TP).

# Installation

Après avoir installé [**Roborobo**](https://github.com/nekonaute/roborobo4/), vous devez:
- cloner ce dépôt : _git clone https://github.com/nekonaute/SU-LU3IN025-robots.git_
- pour tester:
  - _conda activate roborobo_
  - _python comportement.py_

# Remarques spécifique à l'utilisation à la PPTI

Remarques pour l'installation de _roborobo_ à la PPTI:
- vous devez configurer le proxy: _git config --global http.proxy http://proxy:3128_
- utilisez _conda_ (et pas _pip_)
- ne lancez pas les commandes _sudo apt(...)_ (les paquets sont déjà installés)
- lors de la commande _conda activate roborobo_, conda demande parfois de configurer le shell avec la commande _conda init_. Utilisez _conda init bash_ (puis quitter/relancer le shell). (2023/4/3: problème avec tcsh)
- utilisez une version de Python strictement différente de la version 3.10 (ex.: _python3.9_ si présente). Attention à bien vérifier que la version de python est correcte dans l'environnement conda, par rapport à celle accessible par défaut en ligne de commande. 
- votre quota doit être suffisant pour installer et exécuter roborobo (env. 3.5go)

Problèmes classiques : voir la section [**Trouble Shooting**](https://github.com/nekonaute/roborobo4/blob/main/README.md) de Roborobo (tout en bas de la page).

Si vous êtes sous Windows, ou si pour une raison ou une autre vous n'arrivez pas à installer Roborobo sur votre distribution Linux ou MacOS, nous vous suggérons d'installer le logiciel Virtualbox, et d'utiliser une machine virtuelle Linux Ubuntu. Courant 2023, Roborobo ne semblait pas s'installer correctement sur Mac M1 (ceci semble être résolu fin 2023).

# Instructions pour les TPs et le projet

Ce repository contient trois fichiers décrivant les sujets des deux TPs et le sujet de projet.

* [instructions_TP1.md](https://github.com/nekonaute/SU-LU3IN025-robots/blob/main/instructions_TP1.md): TP sur la conception de comportement. Braitenberg et architecture de subsomption. 
* [instructions_TP2.md](https://github.com/nekonaute/SU-LU3IN025-robots/blob/main/instructions_TP2.md): TP sur l'optimisation de comportement pour un robot autonome (recherche aléatoire, puis algorithmes génétiques).
* [instructions_projet.md](https://github.com/nekonaute/SU-LU3IN025-robots/blob/main/instructions_projet.md): description du projet.

Bon courage !
