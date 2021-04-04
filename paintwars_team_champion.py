# Nicolas
# 2021-03-31
#
# comportement par défaut

def get_team_name():
    return "Professor X"

def step(robotId, sensors):

    translation = 1
    rotation = 0
    if sensors["sensor_front_left"]["distance"] < 1 or sensors["sensor_front"]["distance"] < 1:
        rotation = 0.5
    elif sensors["sensor_front_right"]["distance"] < 1:
        rotation = -0.5

    return translation, rotation
