"""@package Canary.Model.NearbyHazard

NearbyHazard is a subclass of Model
"""

import copy
from Model import Model

nearby_hazard = {
	'latitude': 0.0,
	'longitude' : 0.0,
	'description' : "",
	'severity': 0
}

class NearbyHazard(Model):
	def __init__(self):
		super(NearbyHazard, self).__init__()