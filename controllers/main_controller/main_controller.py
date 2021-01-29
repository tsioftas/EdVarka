"""main_controller controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot

# create the Robot instance.
robot = Robot()

# get the time step of the current world.
timestep = int(robot.getBasicTimeStep())

# GPS and inertial unit
gps = robot.getDevice("gps")
inertial_unit = robot.getDevice("inertial unit")
gps.enable(timestep)
inertial_unit.enable(timestep)

# propeller motors
lpm = robot.getDevice("left_propeller_motor")
lpm.setPosition(float('+inf'))
lpm.setVelocity(-5)
rpm = robot.getDevice("right_propeller_motor")
rpm.setPosition(float('+inf'))
rpm.setVelocity(5)

# You should insert a getDevice-like function in order to get the
# instance of a device of the robot. Something like:
#  motor = robot.getMotor('motorname')
#  ds = robot.getDistanceSensor('dsname')
#  ds.enable(timestep)

# Main loop:
# - perform simulation steps until Webots is stopping the controller
while robot.step(timestep) != -1:
    target_position = gps.getValues()
    print(target_position)
    # Read the sensors:
    # Enter here functions to read sensor data, like:
    #  val = ds.getValue()

    # Process sensor data here.

    # Enter here functions to send actuator commands, like:
    #  motor.setPosition(10.0)
    pass

# Enter here exit cleanup code.
