import utils
import math

class robot_movement:
    def __init__(self, hardware_interface):
        self.hi = hardware_interface
        # constants
        self.FACING_THRESHOLD = math.radians(5)
        self.BOAT_ROTATION_ACCELERATION_GAIN = 1
        self.BOAT_ROTATION_DECELERATION_GAIN = -1
        self.SLOW_DOWN_ANGLE = math.radians(10)

    def get_angle_to_target(self, target_position):
        own_azimuth = self.hi.get_compass_reading()
        gps_reading = self.hi.get_gps_values()
        own_position = utils.position(gps_reading[0], gps_reading[1])
        azimuth_to_target = utils.get_angle_between(own_position, target_position)
        return azimuth_to_target - own_azimuth
    
    def is_facing(self, target_position):
        angle_to_target = self.get_angle_to_target(target_position)
        return abs(angle_to_target) < self.FACING_THRESHOLD
    
    def face(self, target_position):
        if self.is_facing(target_position):
            self.hi.set_left_propeller_velocity(0)
            self.hi.set_right_propeller_velocity(0)
        angle_to_turn = self.get_angle_to_target(target_position)
        sign = angle_to_turn / abs(angle_to_turn)
        gain = self.BOAT_ROTATION_ACCELERATION_GAIN
        if abs(angle_to_turn) < self.SLOW_DOWN_ANGLE:
            gain = self.BOAT_ROTATION_DECELERATION_GAIN
        rotation_velocity = sign*gain
        self.hi.set_left_propeller_velocity(rotation_velocity)
        self.hi.set_right_propeller_velocity(-rotation_velocity)

