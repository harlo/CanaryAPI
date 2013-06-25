"""@package Canary.Asset.Nest

Nest is a subclass of Asset
"""

from asset import Asset

members = []
devices = []

class Nest(Asset):	
	
	def __init__(self, inflate=None):
		super(Nest, self).__init__()
		
		self.members = members
		self.devices = devices
		
	def create(self):
		"""Creates a new Nest, and sets its id."""
		super(Nest, self).create()