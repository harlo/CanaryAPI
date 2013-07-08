__metaclass__ = type

class Asset():
	"""The Asset superclass encapsulates all entities (Users, Nests, Devices).  Its acceptedKeys indicates which users may have access to its methods."""
	
	entityId = None
	acceptedKeys = []
	pingProtocol = None
	assetCache = None
	
	def __init__(self, inflate=None):
		print "HELLO ASSET"
		
	def inflate(self, inflate):
		"""Populates the Asset from values in the Canary Datastore."""

		print "inflating asset"
		
	def emit(self):
		return self.__dict__
		
	def ping(self, message=None):
		"""Pings the asset according to its pingProtocol (Google GCM, iOS Push Notification, or other protocol)."""
		
		print "pinging asset"