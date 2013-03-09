import sys
import re
import os
import math


def load_points(datafile):
	


class Point2D:
	def __init__(self, x=0.0, y=0.0):
		self.x = float(x)
		self.y = float(y)
	
	def dist_between(self, other):
		# Compute the distance between this point and another point
		xsq = (self.x - other.x) * (self.x - other.x)
		ysq = (self.y - other.y) * (self.y - other.y)
		return math.sqrt(xsq + ysq)
		
		
points = range(10)
PointList = []
for I in points:
	for J in points:
		tmp = Point2D(0,0)
		tmp.x = (I+1)
		tmp.y = (J+1)
		PointList.append(tmp)
		#print"(%.1f, %.1f)" % (tmp.x, tmp.y)
		
#print PointList[0].x

#for I in points:
#	for J in points:
#		temp1 = PointList[]
		
for I in PointList:
	print I.dist_between(PointList[0])