# Nicolas
# 2021-03-31

from pyroborobo import Pyroborobo, Controller, AgentObserver, WorldObserver, CircleObject, SquareObject, MovableObject
# from custom.controllers import SimpleController, HungryController
import numpy as np
import random

from paintwars_config import *

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

rob = 0

offset_x = 36
offset_y = 36
edge_width = 28
edge_height = 28

scores = {"nobody":0,"Team Red":0,"Team Blue":0}
tiles = []

class MyController(Controller):

    def __init__(self, wm):
        super().__init__(wm)
        if self.id < 8:
            self.team_name = "Team Red"
            self.set_color(255,0,0)
        elif self.id < 16:
            self.team_name = "Team Blue"
            self.set_color(0, 0, 255)
        else:
            print ("[ERROR] 16 robots max.")
            exit(-1)

    def reset(self):
        return

    def step(self):
        global stepRedTeam, stepBlueTeam

        sensors = {}

        sensors["sensor_left"] = {"distance": self.get_distance_at(0), "isRobot": self.get_robot_id_at(0) != -1, "isSameTeam": False}
        sensors["sensor_front_left"] = {"distance": self.get_distance_at(1), "isRobot": self.get_robot_id_at(1) != -1, "isSameTeam": False}
        sensors["sensor_front"] = {"distance": self.get_distance_at(2), "isRobot": self.get_robot_id_at(2) != -1, "isSameTeam": False}
        sensors["sensor_front_right"] = {"distance": self.get_distance_at(3), "isRobot": self.get_robot_id_at(3) != -1, "isSameTeam": False}
        sensors["sensor_right"] = {"distance": self.get_distance_at(4), "isRobot": self.get_robot_id_at(4) != -1, "isSameTeam": False}
        sensors["sensor_back_right"] = {"distance": self.get_distance_at(5), "isRobot": self.get_robot_id_at(5) != -1, "isSameTeam": False}
        sensors["sensor_back"] = {"distance": self.get_distance_at(6), "isRobot": self.get_robot_id_at(6) != -1, "isSameTeam": False}
        sensors["sensor_back_left"] = {"distance": self.get_distance_at(7), "isRobot": self.get_robot_id_at(7) != -1, "isSameTeam": False}

        if sensors["sensor_left"]["isRobot"]:
            sensors["sensor_left"]["isSameTeam"] = self.get_robot_controller_at(0).team_name == self.team_name
        if sensors["sensor_front_left"]["isRobot"]:
            sensors["sensor_front_left"]["isSameTeam"] = self.get_robot_controller_at(1).team_name == self.team_name
        if sensors["sensor_front"]["isRobot"]:
            sensors["sensor_front"]["isSameTeam"] = self.get_robot_controller_at(2).team_name == self.team_name
        if sensors["sensor_front_right"]["isRobot"]:
            sensors["sensor_front_right"]["isSameTeam"] = self.get_robot_controller_at(3).team_name == self.team_name
        if sensors["sensor_right"]["isRobot"]:
            sensors["sensor_right"]["isSameTeam"] = self.get_robot_controller_at(4).team_name == self.team_name
        if sensors["sensor_back_right"]["isRobot"]:
            sensors["sensor_back_right"]["isSameTeam"] = self.get_robot_controller_at(5).team_name == self.team_name
        if sensors["sensor_back"]["isRobot"]:
            sensors["sensor_back"]["isSameTeam"] = self.get_robot_controller_at(6).team_name == self.team_name
        if sensors["sensor_back_left"]["isRobot"]:
            sensors["sensor_back_left"]["isSameTeam"] = self.get_robot_controller_at(7).team_name == self.team_name

        # pour l'orientation relative: comparer self.absolute_orientation et self.get_robot_controller_at(index).absolute_orientation

        if self.team_name == "Team Red":
            translation, rotation = step_red_team(self.id % (len(rob.controllers) / 2), sensors)
        elif self.team_name == "Team Blue":
            translation, rotation = step_blue_team(self.id % (len(rob.controllers) / 2), sensors)

        self.set_translation(translation)
        self.set_rotation(rotation)

        # track meetings
        '''
        for i in range(self.nb_sensors):
            rob = self.get_robot_id_at(i)
            if rob > 0:
                self.agents_met.add(rob)
                #self.get_robot_instance_at(rob)
                robId = self.get_robot_id_at(i)
                robCtl = self.get_robot_controller_at(i)
        '''
        # how to access others
        # controllers = rob.controllers
        # for c in controllers: # costly!
        #    c.check()
        # print(rob.iterations) # marche pas.

    def check(self):
        # print (self.id)
        return True


# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

class MyAgentObserver(AgentObserver):
    def __init__(self, wm):
        super().__init__(wm)
        self.arena_size = Pyroborobo.get().arena_size

    def reset(self):
        super().reset()
        return

    def step_pre(self):
        super().step_pre()
        return

    def step_post(self):
        super().step_post()
        return


# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

class MyWorldObserver(WorldObserver):
    def __init__(self, world):
        super().__init__(world)
        rob = Pyroborobo.get()

    def init_pre(self):
        super().init_pre()

    def init_post(self):
        global offset_x, offset_y, edge_width, edge_height, tiles, arenaIndexSelector, invertStartingPosition, rob

        super().init_post()

        arena = get_arena(arenaIndexSelector)

        for i in range(len(arena)):
            for j in range(len(arena[0])):
                if arena[i][j] == 1:
                    block = BlockObject()
                    block = rob.add_object(block)
                    block.soft_width = 0
                    block.soft_height = 0
                    block.solid_width = edge_width
                    block.solid_height = edge_height
                    block.set_color(164, 128, 0)
                    block.set_coordinates(offset_x + j * edge_width, offset_y + i * edge_height)
                    # print ("i,j=",i,j)
                    retValue = block.can_register()
                    # print("Register block (",block.get_id(),") :", retValue)
                    block.register()
                    block.show()
                elif arena[i][j] == 2:
                    tile = Tile()
                    tile = rob.add_object(tile)
                    tiles.append(tile)
                    tile.radius = 0
                    tile.footprint_radius = 14
                    tile.soft_width = 28
                    tile.soft_height = 28
                    tile.solid_width = 0
                    tile.solid_height = 0
                    tile.set_color(192, 200, 0)
                    tile.set_footprint_color(255, 255, 255)
                    tile.set_coordinates(offset_x + j * edge_width, offset_y + i * edge_height)
                    retValue = tile.can_register()
                    # print("Register tile (",tile.get_id(),") :", retValue)
                    tile.register()
                    tile.unregister()
                    tile.register()
                    tile.show()

        counter = 0
        for robot in rob.controllers:
            if robot.team_name == "Team Red":
                if invertStartingPosition == False:
                    x = offset_x + 1 * edge_width
                    y = offset_y + 7 * edge_height + edge_height / 2 + (counter * edge_height * 2 - edge_height / 2)
                    robot.set_absolute_orientation(0)
                    robot.set_position(x, y)
                else:
                    x = offset_x + 25 * edge_width
                    y = offset_y + 7 * edge_height + edge_height / 2 + (counter * edge_height * 2 - edge_height / 2)
                    robot.set_absolute_orientation(180)
                    robot.set_position(x, y)
                first = False
            elif robot.team_name == "Team Blue":
                if invertStartingPosition == False:
                    x = offset_x + 25 * edge_width
                    y = offset_y + 7 * edge_height + edge_height / 2 + (counter % 8 * edge_height * 2 - edge_height / 2)
                    robot.set_absolute_orientation(180)
                    robot.set_position(x, y)
                else:
                    x = offset_x + 1 * edge_width
                    y = offset_y + 7 * edge_height + edge_height / 2 + (counter % 8 * edge_height * 2 - edge_height / 2)
                    robot.set_absolute_orientation(0)
                    robot.set_position(x, y)
            counter += 1

    def step_pre(self):
        super().step_pre()
        # pyrob = Pyroborobo.get()
        # if pyrob.iterations == 0:
        #    print ("ZERO")

    def step_post(self):
        global tiles, rob

        super().step_post()
        # for ctlrob in rob.controllers:
        #    print(ctlrob.inspect())
        if (rob.iterations % 100 == 0):
            for key in scores.keys():
                scores[key] = 0
            for t in tiles:
                if t.owner not in scores:
                    scores[t.owner] = 1
                else:
                    scores[t.owner] += 1
            if invertStartingPosition == False:
                print("Scores at iteration #", rob.iterations, ": { Team Red:", scores["Team Red"],", Team Blue:",scores["Team Blue"],"}")
            else:
                print("Scores at iteration #", rob.iterations, ": { Team Blue:",
                      scores["Team Blue"], ", Team Red:", scores["Team Red"],"}" )


# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

class Tile(SquareObject):  # CircleObject):

    def __init__(self, id=-1, data={}):
        super().__init__(id, data)
        self.owner = "nobody"

    def step(self):
        return

    def is_walked(self, id_):
        global rob
        robot = rob.controllers[id_]
        # print ("[TEST]", robot.get_id())
        if robot.team_name == "Team Red":
            self.set_footprint_color(255, 240, 250)
            self.owner = robot.team_name
        elif robot.team_name == "Team Blue":
            self.set_footprint_color(240, 240, 255)
            self.owner = robot.team_name
        return


# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

class BlockObject(SquareObject):
    def __init__(self, id=-1, data={}):
        super().__init__(id, data)

    def step(self):
        # self.unregister()
        # self.register()
        # self.show()
        return

    def is_walked(self, id_):
        return


# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

def main():
    global rob

    rob = Pyroborobo.create(
        "config/paintwars.properties",
        controller_class=MyController,
        world_observer_class=MyWorldObserver,
        #        world_model_class=PyWorldModel,
        agent_observer_class=MyAgentObserver,
        object_class_dict={},
        override_conf_dict={"gDisplayMode": simulation_mode} # defined in paintwars_config
    )

    rob.start()

    print("# ___________________________ #")
    print("#                             #")
    print("#    Welcome to Paint Wars    #")
    print("# ___________________________ #")
    print("#")
    print("#")
    print("# Team RED :",get_name_red_team())
    print("# Team BLUE:",get_name_blue_team())
    print("#")
    print("#")

    rob.update(2001)
    rob.close()

    print("\n=-=-=-=-=-=-=-=-=\n= FINAL RESULTS =\n=-=-=-=-=-=-=-=-=\n")
    #print(scores)
    print("Team Red  :", scores["Team Red"])
    print("Team Blue :", scores["Team Blue"])
    print("tiles left:", scores["nobody"])
    print("")

    s = ""
    if scores["Team Red"] > scores["Team Blue"]:
        s += "# Team RED won! Congratulations " + get_name_red_team() + " ! #"
    elif scores["Team Red"] < scores["Team Blue"]:
        s += "# Team BLUE won! Congratulations " + get_name_blue_team() + " ! #"
    else:
        s += "Draw! (no winner)"

    print (len(s)*"#")
    print (s)
    print (len(s)*"#")
    print("")

if __name__ == "__main__":
    main()
