"""@package Canary.Asset.Device

Device is a subclass of Asset
"""

import copy
from asset import Asset

status = {
	'battery': 0.0,
	'monoxide': 0.0,
	'air_quality': 0.0	
}

class Device(Asset):	
	def __init__(self, inflate=None):
		super(Device, self).__init__()
				
	def create(self):
		"""Creates a new Device, and sets its id."""
		super(Device, self).create()
		
		self.status = copy.deepcopy(status)