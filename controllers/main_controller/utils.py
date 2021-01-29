import math

class position:

    def __init__(self, longitude, latitude):
        self.longitude = longitude
        self.latitude = latitude
    

# Returns the clockwise angle from the north axis of position1 to position 2
# (azimuth)
def get_angle_between(position1, position2):
        atan = math.atan2(position2.latitude - position1.latitude,
                          position2.longitude - position1.longitude)
        #print(atan)
        azimuth = -atan + math.pi/2
        if azimuth > math.pi:
            azimuth -= 2*math.pi
        return azimuth
        
point1 = position(0, 0)
point2 = position(0, 1)

print(math.degrees(get_angle_between(point1, point2)))
