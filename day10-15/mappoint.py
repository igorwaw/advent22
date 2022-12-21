#!/usr/bin/python3

class Mappoint:
    x: int
    y: int
    def __init__(self, x,y):
        self.x=x
        self.y=y
    
    def __str__(self):
        return f"{self.x},{self.y}"

    def __repr__(self):
        return f"{self.x},{self.y}"



class PointWithDistance:
    distance: int
    point: Mappoint
    
    def __init__(self, distance: int, point: Mappoint):
        self.point=point
        self.distance=distance

    def __str__(self):
        return f"{self.point.x},{self.point.y} distance {self.distance}"

    def __repr__(self):
        return f"{self.point.x},{self.point.y} distance {self.distance}"

    def __lt__(self, other):
        return self.distance<other.distance

    def __gt__(self, other):
        return self.distance>other.distance
