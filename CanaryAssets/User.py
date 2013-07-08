"""@package Canary.Asset.User

User is a subclass of Asset
"""

from Asset import Asset

nests = []

class User(Asset):
	"""The User class"""
	
	def __init__(self, inflate=None):
		super(User, self).__init__(inflate)
			
	def create(self):
		"""Creates a new User, and sets its id."""
		super(User, self).create()
		
		self.nests = nests
					
		print "creating new User as %s" % self.entityId
	
	def addToNest(self, nestId=None):
		"""Adds User to a Nest"""
		self.nests.append(nestId)
		
		print "adding user %s to nest %s" % (self.entityId, nestId)
		
	def removeFromNest(self, nestId=None):
		"""Removes User from a Nest"""
		self.nests.remove(nestId)
		
		print "removing user %s from nest %s" % (self.entityId, nestId)