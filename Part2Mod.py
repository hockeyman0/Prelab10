#! /usr/bin/env python2.6

#$Author$
#$Date$
#$Revision$
#$HeadURL$

import sys
import re
import os
import math

class Point3D:
	def __init__(self, x, y, z):
		self.x = float(x)
		self.y = float(y)
		self.z = float(z)
		
	def distance_from(self, other):
		tempx = self.x - other.x
		tempy = self.y - other.y
		tempz = self.z - other.z
		tempall = (tempz * tempz) + (tempy * tempy) + (tempz * tempz)
		tempall = math.sqrt(tempall)
		return tempall
		
		
		
	def nearest_point(self, others):
		mini = self.distance_from(others[0])
		#point = Point3D(0,0,0)
		#point.x = others[0].x
		#point.y = others[0].y
		#point.z = others[0].z
		point = others[0]
		for other in others:
			temp = self.distance_from(other)
			if temp < mini:
				mini = temp
				point = other
		
		return point
		
		
		
		
class PointSet:
	def __init__(self):
		self.points = []
		
	def add_point(self, p):
		self.points.append(p)
		
	def get_num_points(self):
		return len(self.points)
		
	def compute_bounding_box(self):
		pointxp = self.points[0].x
		pointxn = self.points[0].x
		pointyp = self.points[0].y
		pointyn = self.points[0].y 
		pointzp = self.points[0].z
		pointzn = self.points[0].z
		for point in self.points:
			if point.x > pointxp:
				pointxp = point.x
			if point.x < pointxn:
				pointxn = point.x
			if point.x > pointxp:
				pointyp = point.y
			if point.x < pointxn:
				pointyn = point.y
			if point.x > pointxp:
				pointzp = point.z
			if point.x < pointxn:
				pointzn = point.z
				
		finalhigh = Point3D(pointxp, pointyp, pointzp)
		finallow = Point3D(pointxn, pointyn, pointzn)

		
		final = ["(%.3f, %.3f, %.3f)" % (pointxp, pointyp, pointzp), "(%.3f, %.3f, %.3f)" % (pointxn, pointyn, pointzn)]
		return tuple(final)
		
		
	def compute_nearest_neighbors(self, other):
		final = []
		for point in self.points:
			close = point.nearest_point(other.points)
			tmp = ["(%.3f, %.3f, %.3f)" % (point.x, point.y, point.z),"(%.3f, %.3f, %.3f)" % (close.x, close.y, close.z)]
			tmp = tuple(tmp)
			final.append(tmp)
			
		return final
									