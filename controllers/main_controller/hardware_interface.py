from controller import Robot

class hardware_interface:

    def __init__(self, robot):
        self.robot = robot

    def get_gps_values(self):
        return self.robot.getDevice("gps").getValues()

    def set_left_propeller_position(self, p):
        left_prop = self.robot.getDevice("left_propeller_motor")
        self.set_propeller_position(left_prop, p)

    def set_left_propeller_velocity(self, v):
        left_prop = self.robot.getDevice("left_propeller_motor")
        self.set_propeller_velocity(left_prop, v)

    def set_right_propeller_position(self, p):
        right_prop = self.robot.getDevice("right_propeller_motor")
        self.set_propeller_position(right_prop, p)

    def set_right_propeller_velocity(self, v):
        right_prop = self.robot.getDevice("right_propeller_motor")
        self.set_propeller_velocity(right_prop, v)

    def set_propeller_position(self, propeller, p):
        propeller.setPosition(p)

    def set_propeller_velocity(self, propeller, v):
        propeller.setVelocity(v)

