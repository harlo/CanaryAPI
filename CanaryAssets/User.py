"""@package Canary.Asset.User

User is a subclass of Asset
"""
import copy
from Asset import Asset

profile = {
	'alias': "",
	'email': "",
	'phone_number': "",
	'address': "",
	'city': "",
	'state': "",
	'zip': ""
}

class User(Asset):
	"""The User class"""
	
	def __init__(self, inflate=None):
		super(User, self).__init__(inflate)
		
		self.nests = []
		self.profile = copy.deepcopy(profile)
			
	def addToNest(self, nestId=None):
		"""Adds User to a Nest"""
		self.nests.append(nestId)
		
		print "adding user %s to nest %s" % (self.entityId, nestId)
		
	def removeFromNest(self, nestId=None):
		"""Removes User from a Nest"""
		self.nests.remove(nestId)
		
		print "removing user %s from nest %s" % (self.entityId, nestId)