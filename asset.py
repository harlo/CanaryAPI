"""@package Canary.Asset

This is a test!
"""

__metaclass__ = type

class Asset():
	"""The Asset superclass encapsulates all entities (Users, Nests, Devices).  Its acceptedKeys indicates which users may have access to its methods."""
	
	entityId = None
	acceptedKeys = []
	pingProtocol = None
	
	def __init__(self):
		print "HELLO ASSET"
		
	def create(self):
		"""Creates a new Asset, and sets its id."""
		self.entityId = "HERPIE DERP"
		print "creating new asset"
		
	def emit(self):
		return self.__dict__
		
	def ping(self, message=None):
		"""Pings the asset according to its pingProtocol (Google GCM, iOS Push Notification, or other protocol)."""
		
		print "pinging asset"