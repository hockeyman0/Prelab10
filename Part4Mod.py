#! /usr/bin/env python

#$Author$
#$Date$
#$Revision$
#$HeadURL$

import sys
import os

class Expression:
	def __init__(self):
		# Function: Constructs a new expression
		pass
	
	def evaluate(self, variables):
		# Function: Evaluates the expression and returns the real valued result of the expression (e.g. 5.5 + 2 evaluates to 7.5)
		# Arguments: 
		# 1. variables - A dictionary mapping variable names to real values
		pass
		
	def __str__(self):
		# Functions: (Special) Returns a string representation of this expression
		# This function is called when the object is passes to the str() function
		return ""
		
	def clone(self):
		pass
		
	def __add__(self, rhs):
		return BinaryExpression(self, rhs, "+")
		
	def __sub__(self, rhs):
		return BinaryExpression(self, rhs, "-")
		
	def __mul__(self, rhs):
		return BinaryExpression(self, rhs, "*")
		
	def __div__(self, rhs):
		return BinaryExpression(self, rhs, "/")
		
class RealValuedExpression(Expression):
	def __init__(self, value):
		self.value = float(value)
		#print self.value
		#pass
		
	def evaluate(self, variables):
		#return variables.get(self)
		return self.value
		pass
		
	def __str__(self):
		return str(self.value)
		
	def clone(self):
		cloned = self
		return cloned
		
		

class BinaryExpression(Expression):
	def __init__(self, lhs, rhs, op):
		self.lhs = lhs
		#print lhs.evaluate
		self.rhs = rhs
		self.op = op

	def evaluate(self, variables):
		out = None
		if self.op == "+":
			out = self.lhs.evaluate(variables) + self.rhs.evaluate(variables)
		if self.op == "-":
			out = self.lhs.evaluate(variables) - self.rhs.evaluate(variables)
		if self.op == "*":
			out = self.lhs.evaluate(variables) * self.rhs.evaluate(variables)
		if self.op == "/":
			out = self.lhs.evaluate(variables) / self.rhs.evaluate(variables)
			
		return out

	def __str__(self):
		return ("(%s%s%s)" % (self.lhs, self.op, self.rhs))
		
		
	def clone(self):
		cloned = self
		return cloned
		
		

class VariableExpression(Expression):
	def __init__(self, variable_name):
		self.variable_name = variable_name
	
	def evaluate(self, variables):
		return variables.get(self.variable_name)
			
	def __str__(self):
		return ("%s" % (self.variable_name))
		
	def clone(self):
		cloned = self
		return cloned
