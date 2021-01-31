import utils
import math

class robot_movement:
    def __init__(self, hardware_interface):
        self.hi = hardware_interface
        # constants
        self.FACING_THRESHOLD = math.radians(5)
        self.DISTANCE_THRESHOLD = 1.5 # meter(s)
        # PΙD controller for facing
        self.INCLUDE_I_TERM_THRESHOLD_F = math.radians(7)
        self.last_f_error = 0
        self.f_Kp = 2.5
        self.f_Kd = 7500
        self.f_Ki = 0.3
        # PID controller for travelling
        self.INCLUDE_I_TERM_THRESHOLD_T = 0
        self.last_t_error = 0
        self.t_Kp = 1
        self.t_Kd = 1
        self.t_Ki = 0

    def get_angle_to_target(self, target_position):
        own_azimuth = self.hi.get_compass_reading()
        gps_reading = self.hi.get_gps_values()
        own_position = utils.position(gps_reading[1], gps_reading[0])
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
        error_derivative = (error - self.last_f_error) / self.hi.timestep
        self.last_f_error = error
        error_integral = error * self.hi.timestep
        include_i_term = 0
        if abs(error) < self.INCLUDE_I_TERM_THRESHOLD_F:
            include_i_term = 1
        rotation_velocity = (self.f_Kp*error + self.f_Kd*error_derivative + include_i_term*self.f_Ki*error_integral)
        self.hi.set_left_propeller_velocity(rotation_velocity)
        self.hi.set_right_propeller_velocity(-rotation_velocity)
    
    def get_distance_to_target(self, target_position):
        gps_reading = self.hi.get_gps_values()
        own_position = utils.position(gps_reading[0], gps_reading[1])
        return utils.get_distance_between(own_position, target_position)

    def is_in_proximity(self, target_position):
        dist = self.get_distance_to_target(target_position)
        return dist < self.DISTANCE_THRESHOLD
    
    def move_towards(self, target_position):
        #self.hi.right_propeller.setVelocity(2)
        #self.hi.left_propeller.setVelocity(2)
        # if not self.is_facing(target_position):
        #     # maybe call self.face(target_position)?
        #     print("IF")
        #     return
        # error = self.get_distance_to_target(target_position)
        # error_derivative = (error - self.last_t_error) / self.hi.timestep
        # self.last_t_error = error
        # error_integral = error * self.hi.timestep
        # include_i_term = 0
        # if abs(error) < self.INCLUDE_I_TERM_THRESHOLD_T:
        #     include_i_term = 1
        # rotation_velocity = (self.t_Kp*error + self.t_Kd*error_derivative + include_i_term*self.t_Ki*error_integral)
        # self.hi.set_right_propeller_velocity(rotation_velocity)
        # self.hi.set_left_propeller_velocity(rotation_velocity)

