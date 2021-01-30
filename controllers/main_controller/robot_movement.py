import utils
import math

class robot_movement:
    def __init__(self, hardware_interface):
        self.hi = hardware_interface
        # constants
        self.FACING_THRESHOLD = math.radians(5)
        # PΙD controller
        self.last_error = 0
        self.Kp = 2.5
        self.Kd = 7500
        self.Ki = 50

    def get_angle_to_target(self, target_position):
        own_azimuth = self.hi.get_compass_reading()
        gps_reading = self.hi.get_gps_values()
        own_position = utils.position(gps_reading[0], gps_reading[1])
        azimuth_to_target = utils.get_angle_between(own_position, target_position)
        ret = azimuth_to_target - own_azimuth
        if abs(ret) > math.pi:
            if ret < 0:
                ret += 2*math.pi
            else:
                ret -= 2*math.pi
        return ret
    
    def is_facing(self, target_position):
        angle_to_target = self.get_angle_to_target(target_position)
        return abs(angle_to_target) < self.FACING_THRESHOLD
    
    def face(self, target_position):
        error = self.get_angle_to_target(target_position)
        error_derivative = (error - self.last_error) / self.hi.timestep
        self.last_error = error
        error_integral = error_derivative * self.hi.timestep
        include_i_term = 0
        if abs(error) < math.radians(30):
            include_i_term = 1
        rotation_velocity = (self.Kp*error + self.Kd*error_derivative - include_i_term*self.Ki*error_integral)
        #rotation_velocity = rotation_velocity*rotation_velocity*rotation_velocity/abs(rotation_velocity)
        self.hi.set_left_propeller_velocity(rotation_velocity)
        self.hi.set_right_propeller_velocity(-rotation_velocity)

