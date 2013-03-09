import sys
import re
import os
import math


def load_points(datafile):
	if (os.access(datafile, os.R_OK) == 0):
		sys.exit(1)
	InFile = open(datafile, "r")
	


class Point2D:
	def __init__(self, x=0.0, y=0.0):
		self.x = float(x)
		self.y = float(y)
	
	def dist_between(self, other):
		# Compute the distance between this point and another point
		xsq = (self.x - other.x) * (self.x - other.x)
		ysq = (self.y - other.y) * (self.y - other.y)
		return math.sqrt(xsq + ysq)
		
		
class MyPoint2D(Point2D):
	def __init__(self, x, y):
		Point2D.__init__(self,0.0,0.0)
		self.x = float(x)
		self.y = float(y)
		
	def get_max_coord(self):
		if self.x > self.y:
			return self.x
		else:
			return self.y
	def get_min_coord(self):
		if self.x < self.y:
			return self.x
		else:
			return self.y
		
		
points = range(10)
PointList = []
for I in points:
	for J in points:
		tmp = Point2D(0,0)
		tmp.x = (I+1)
		tmp.y = (J+1)
		PointList.append(tmp)

		
for I in PointList:
	print I.dist_between(PointList[0])
	
	
testpoint = MyPoint2D(5,9)
print testpoint.get_max_coord()
print testpoint.get_min_coord()