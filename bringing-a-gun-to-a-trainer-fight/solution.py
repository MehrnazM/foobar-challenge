import math

class Room:

    def __init__(self, room, shooter, trainer, distance):
        self.room_x, self.room_y = room
        self.shooter_x, self.shooter_y = shooter
        self.trainer_x, self.trainer_y = trainer
        self.distance = distance

    def get_distance(self, point):
        x, y = point
        return math.sqrt(((x-self.shooter_x)**2)+((y-self.shooter_y)**2))
    
    def get_angle(self,point):
        x, y = point
        return math.atan2(y-self.shooter_y, x-self.shooter_x)
    
    
    def get_mirrored(self):
        max_x = self.shooter_x + self.distance 
        max_y = self.shooter_y + self.distance
        mirrored = set()
        t_x = self.trainer_x
        s_x = self.shooter_x
        r_x = self.room_x
        while t_x < max_x+1 and s_x < max_x+1:
            t_y = self.trainer_y
            s_y = self.shooter_y
            r_y = self.room_y
            while t_y < max_y+1 and s_y < max_y+1:
                mirrored.update([((t_x,t_y),True),((-t_x,t_y),True),((t_x,-t_y),True),((-t_x,-t_y),True)])
                mirrored.update([((s_x,s_y),False),((-s_x,s_y),False),((s_x,-s_y),False),((-s_x,-s_y),False)])
                t_y = t_y + (r_y - t_y)*2
                s_y = s_y + (r_y - s_y)*2
                r_y += self.room_y
            t_x = t_x + (r_x - t_x)*2
            s_x = s_x + (r_x - s_x)*2
            r_x += self.room_x
        return mirrored
    
    def filtered(self):
        points = self.get_mirrored()
        angles = {}
        for p in points:
            point = p[0]
            dist = self.get_distance(point)
            angle = self.get_angle(point)
            if 0 < dist <= self.distance and (angle not in angles or angles[angle][1] > dist):
                angles[angle] = [p,dist]
        return angles

def solution(dimensions, your_position, trainer_position, distance):
    room = Room(dimensions,your_position,trainer_position,distance)
    points = room.filtered()
    count = 0
    angles = points.keys()
    for angle in angles:
        p = points[angle][0]
        if p[1]:
            count += 1
    return count