"""@package Canary.Utils.Authentication

Methods available for managing authentication between entities.
"""

def grantAccessToEntity(entity_id):
	"""Grants access to an entity (User, Device, Nest) to perform protected actions.  The bearer's cookie must contain a key that the entity can recognize."""

	print "granting access to entity_id % s" % entity_id