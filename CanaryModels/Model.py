__metaclass__ = type

min_value = 0.0
max_value = 0.0
version = "1.0.0"

class Model():
	"""The Model superclass encapsulates all data objects that record, calculate, and emit real-time metric data, such as temperature readings, co2, battery, etc."""
	
	def __init__(self):
		print "HELLO Model"
		
	def calculateScore(self):
		"""Calculates the floating point value of the given metric.  This method must be overridden by the subclass using it, as each metric has a unique way of being calculated."""
		print "calculating my score"
		
	def emit(self):
		"""Returns a json-encoded representation of this object."""
		return self.__dict__