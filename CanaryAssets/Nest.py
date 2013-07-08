"""@package Canary.Asset.Nest

Nest is a subclass of Asset
"""

import copy
from Asset import Asset
from CanaryModels import OutdoorQuality, NearbyHazard

members = []
devices = []
quality = {
	'outdoor': OutdoorQuality(),
	'nearby_hazards': []
}

class Nest(Asset):	
	
	def __init__(self, inflate=None):
		super(Nest, self).__init__(inflate)
		
		self.members = members
		self.devices = devices
		self.quality = copy.deepcopy(quality)
		
	def create(self):
		"""Creates a new Nest, and sets its id."""
		super(Nest, self).create()