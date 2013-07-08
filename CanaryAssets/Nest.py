"""@package Canary.Asset.Nest

Nest is a subclass of Asset
"""

import copy
from Asset import Asset
from CanaryModels import OutdoorQuality, NearbyHazard
from CanaryAssets import User

members = []
devices = []
quality = {
	'outdoor': OutdoorQuality(),
	'nearby_hazards': []
}

class Nest(Asset):	
	
	def __init__(self, inflate=None):
		super(Nest, self).__init__(inflate)
		
		self.owner = User()
		self.members = members
		self.devices = devices
		self.quality = copy.deepcopy(quality)