"""@package Canary.Asset.Device

Device is a subclass of Asset
"""

import copy
from Asset import Asset
from CanaryModels import *

status = {
	'smoke': Smoke(),
	'co': CO(),
	'no2': NO2(),
	'pm2_5' : PM2_5(),
	'pm10': PM10(),
	'co2': CO2(),
	'temperature': Temperature(),
	'battery': Battery()
}

class Device(Asset):	
	def __init__(self, inflate=None):
		super(Device, self).__init__(inflate)

		self.nest = Nest()
		self.status = copy.deepcopy(status)
				
	def addToNest(self, nestId=None):
		"""Adds Device to a Nest"""
		self.nests.append(nestId)
		
		print "adding user %s to nest %s" % (self.entityId, nestId)
		
	def removeFromNest(self, nestId=None):
		"""Removes Device from a Nest"""
		self.nests.remove(nestId)
		
		print "removing user %s from nest %s" % (self.entityId, nestId)