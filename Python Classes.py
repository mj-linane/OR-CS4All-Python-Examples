# PYTHON CLASSES
# HOW TO THINK LIKE A COMPUTER SCIENTIST Chapter 16
import math

# class Point:
#   """ For X,Y coordinates """

#   def __init__(self):
#     """Creates a new point at the origin"""
#     self.x=0
#     self.y=0

# p = Point()         # Instantiate an object of type Point
# q = Point()         # and make a second point


# CLASS VERSION #2 (Using Functions)
# class Point:
#     """ Point class for representing and manipulating x,y coordinates. """

#     def __init__(self, initX, initY):
#         self.x = initX
#         self.y = initY

#     def getX(self):
#         return self.x

#     def getY(self):
#         return self.y

#     def distanceFromOrigin(self):
#         return ((self.x ** 2) + (self.y ** 2)) ** .5


# p = Point(7, 6)
# print(p.getX())
# print(p.getY())
# print(p.distanceFromOrigin())

# CLASS VERSION #3 (Functions outside of class)
# class Point:
#     """ Point class for representing and manipulating x,y coordinates. """

#     def __init__(self, initX, initY):
#         self.x = initX
#         self.y = initY

#     def getX(self):
#         return self.x

#     def getY(self):
#         return self.y

#     def distanceFromOrigin(self):
#         return ((self.x ** 2) + (self.y ** 2)) ** .5

# def distance(point1, point2):
#     xdiff = point2.getX() - point1.getX()
#     ydiff = point2.getY() - point1.getY()

#     dist = math.sqrt(xdiff ** 2 + ydiff ** 2)
#     return dist

# p = Point(4, 3)
# q = Point(0,0)
# print(distance(p, q))

# CLASS STATES USING __str__
class Point:
    """ Point class for representing and manipulating x,y coordinates. """

    def __init__(self, initX, initY):
        """ Create a new point at the given coordinates. """
        self.x = initX
        self.y = initY

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distanceFromOrigin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def __str__(self):
        return "x=" + str(self.x) + ", y=" + str(self.y)


p = Point(7, 6)
print(p)
