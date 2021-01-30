import utils
import math

class robot_movement:
    def __init__(self, hardware_interface):
        self.hi = hardware_interface
        self.FACING_THRESHOLD = math.radians(10)

    def get_angle_to_target(self, target_position):
        own_azimuth = self.hi.get_compass_reading()
        gps_reading = self.hi.get_gps_values()
        own_position = utils.position(gps_reading[0], gps_reading[1])
        azimuth_to_target = utils.get_angle_between(own_position, target_position)
        return azimuth_to_target - own_azimuth
    
    def is_facing(self, target_position):
        angle_to_target = self.get_angle_to_target(target_position)
        return math.abs(angle_to_target) < self.FACING_THRESHOLD
