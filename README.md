# SU-LU3IN025-robots
UE LU3IN025 IA et Jeux, partie Robotique Autonome

# Pré-requis

Vous devez installer le simulateur [**Roborobo**](https://github.com/nekonaute/roborobo4/) sur votre machine avant de commencer. Ce simulateur s'installe facilement sous Linux et sous MacOS en suivant les [instructions](https://github.com/nekonaute/roborobo4/blob/main/README.md).

Remarques pour l'installation de _roborobo_ à la PPTI:
- vous devez configurer le proxy: _git config --global http.proxy http://proxy:3128_
- utilisez _conda_ (et pas _pip_)
- ne lancez pas les commandes _sudo apt(...)_ (les paquets sont déjà installés)
- utilisez _python3.7_, ou tout autre version strictement antérieure à la version 3.10. Attention à bien vérifier que la version de python est correcte dans l'environnement conda. 
- lors de la commande _conda activate roborobo_, conda demande parfois de configurer le shell avec la commande _conda init_. Utilisez _conda init bash_ (puis quitter/relancer le shell). (2023/4/3: problème avec tcsh)
- votre quota doit être suffisant pour installer et exécuter roborobo (env. 3.5go)

Problèmes classiques:
- lors du lancement d'un exemple: 
  - ModuleNotFoundError: No module named 'pyroborobo'
  - ImportError: /lib/x86_64-linux-gnu/libwayland-server.so.0: undefined symbol: ffi_type_uint32, version LIBFFI_BASE_7.0

=> Il s'agit d'un problème avec la version de Python (utilisez une version <=3.9). Ce problème peut se produire lors de l'activation de l'environnement conda, qui utilise une version de Python de celle du système. A priori, pas de problème si on utilise _bash_

Si vous êtes sous Windows, ou si pour une raison ou une autre vous n'arrivez pas à installer Roborobo sur votre distribution Linux ou MacOS, nous vous suggérons d'installer le logiciel Virtualbox, et de créer une machine virtuelle Linux Ubuntu. 

# Instructions pour les TPs et le projet

Ce repository contient trois fichiers décrivant les sujets des deux TPs et le sujet de projet.

* [instructions_TP1.md](https://github.com/nekonaute/SU-LU3IN025-robots/blob/main/instructions_TP1.md): TP sur la conception de comportement. Braitenberg et architecture de subsomption. 
* [instructions_TP2.md](https://github.com/nekonaute/SU-LU3IN025-robots/blob/main/instructions_TP2.md): TP sur l'optimisation de comportement pour un robot autonome (recherche aléatoire, puis algorithmes génétiques).
* [instructions_projet.md](https://github.com/nekonaute/SU-LU3IN025-robots/blob/main/instructions_projet.md): description du projet.

Bon courage !
