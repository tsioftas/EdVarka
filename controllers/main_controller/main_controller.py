"""main_controller controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor

from controller import Robot

from hardware_interface import hardware_interface
from robot_movement import robot_movement
import utils

# create the Robot instance.
robot = Robot()

# get the time step of the current world.
timestep = int(robot.getBasicTimeStep())

hi = hardware_interface(robot)
# enable devices
hi.enable_devices()
# get the propeller running
hi.set_right_propeller_position(float('+inf'))
hi.set_left_propeller_position(float('+inf'))
hi.set_left_propeller_velocity(0)
hi.set_right_propeller_velocity(0)

rm = robot_movement(hi)

# You should insert a getDevice-like function in order to get the
# instance of a device of the robot. Something like:
#  motor = robot.getMotor('motorname')
#  ds = robot.getDistanceSensor('dsname')
#  ds.enable(timestep)

# Main loop:
# - perform simulation steps until Webots is stopping the controller
while robot.step(timestep) != -1:
    cr = hi.get_compass_reading()
    gr = hi.get_gps_values()
    rubbish_pos = utils.position(-1.5166521477594617e-05, 2.059941449563191e-05)
    print("Angle to turn: {}".format(rm.get_angle_to_target(rubbish_pos)))

