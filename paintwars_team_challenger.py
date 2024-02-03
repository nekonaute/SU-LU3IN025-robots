# Projet "robotique" IA&Jeux 2021
#
# Binome:
#  Prénom Nom: _________
#  Prénom Nom: _________
import random


def get_team_name():
    return " Team Red "  # à compléter (comme vous voulez)


# par defaut

# def step(robotId, sensors):

#     translation = 1  # vitesse de translation (entre -1 et +1)
#     rotation = 0  # vitesse de rotation (entre -1 et +1)

#     if (
#         sensors["sensor_front_left"]["distance"] < 1
#         or sensors["sensor_front"]["distance"] < 1
#     ):
#         rotation = 0.5  # rotation vers la droite
#     elif sensors["sensor_front_right"]["distance"] < 1:
#         rotation = -0.5  # rotation vers la gauche

# if (
#     sensors["sensor_front"]["isRobot"] == True
#     and sensors["sensor_front"]["isSameTeam"] == False
# ):
#     enemy_detected_by_front_sensor = True  # exemple de détection d'un robot de l'équipe adversaire (ne sert à rien)

#     return translation, rotation


def get_extended_sensors(sensors):
    for key in sensors:
        sensors[key]["distance_to_robot"] = 1.0
        sensors[key]["distance_to_wall"] = 1.0
        if sensors[key]["isRobot"] == True:
            sensors[key]["distance_to_robot"] = sensors[key]["distance"]
        else:
            sensors[key]["distance_to_wall"] = sensors[key]["distance"]
    return sensors


def step(robotId, sensors):  # <<<<<<<<<------- fonction à modifier pour le TP1

    # sensors: dictionnaire contenant toutes les informations senseurs
    # Chaque senseur renvoie:
    #   la distance à l'obstacle (entre 0  et 1, distance max)
    #   s'il s'agit d'un robot ou non
    #   la distance au robot (= 1.0 s'il n'y a pas de robot)
    #   la distance au mur (= 1.0 s'il n'y a pas de robot)
    # cf. exemple ci-dessous

    # récupération des senseurs

    sensors = get_extended_sensors(sensors)
    print(
        "[robot #",
        robotId,
        "] senseur frontal: (distance à l'obstacle =",
        sensors["sensor_front"]["distance"],
        ")",
        "(robot =",
        sensors["sensor_front"]["isRobot"],
        ")",
        "(distance_to_wall =",
        sensors["sensor_front"]["distance_to_wall"],
        ")",  # renvoie 1.0 si ce n'est pas un mur
        "(distance_to_robot =",
        sensors["sensor_front"]["distance_to_robot"],
        ")",  # renvoie 1.0 si ce n'est pas un robot
    )

    # contrôle moteur. Ecrivez votre comportement de Braitenberg ci-dessous.
    # il est possible de répondre à toutes les questions en utilisant seulement:
    #   sensors["sensor_front"]["distance_to_wall"]
    #   sensors["sensor_front"]["distance_to_robot"]
    #   sensors["sensor_front_left"]["distance_to_wall"]
    #   sensors["sensor_front_left"]["distance_to_robot"]
    #   sensors["sensor_front_right"]["distance_to_wall"]
    #   sensors["sensor_front_right"]["distance_to_robot"]

    translation = 1 * sensors["sensor_front"]["distance"]

    rotation = (-1) * sensors["sensor_front_left"]["distance_to_wall"] + (1) * sensors[
        "sensor_front_right"
    ]["distance_to_wall"]

    # evite wall
    if sensors["sensor_front"]["distance_to_wall"] < 1:
        rotation = -1
    if sensors["sensor_front_left"]["distance_to_wall"] < 1:
        rotation = random.random() / 2
    if sensors["sensor_front_right"]["distance_to_wall"] < 1:
        rotation = -random.random() / 2

    # love robot
    if (
        sensors["sensor_front_left"]["distance_to_robot"] < 1
        and sensors["sensor_front_left"]["isSameTeam"] == False
    ):
        rotation = random.uniform(-1, 0)
    if (
        sensors["sensor_front_right"]["distance_to_robot"] < 1
        and sensors["sensor_front_right"]["isSameTeam"] == False
    ):
        rotation = random.uniform(0, 1)

    # evite notre robot
    if (
        sensors["sensor_front"]["isRobot"] == True
        and sensors["sensor_front"]["isSameTeam"] == True
    ):
        rotation = random.uniform(-1, 1)
    if (
        sensors["sensor_front_right"]["isRobot"] == True
        and sensors["sensor_front_right"]["isSameTeam"] == True
    ):
        rotation = random.uniform(-1, 1)
    if (
        sensors["sensor_front_left"]["isRobot"] == True
        and sensors["sensor_front_left"]["isSameTeam"] == True
    ):
        rotation = random.uniform(-1, 1)

    # limite les valeurs de sortie entre -1 et +1
    translation = max(-1, min(translation, 1))
    rotation = max(-1, min(rotation, 1))

    return translation, rotation

