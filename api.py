"""@package Canary.Api

The main API for the cloud-based service.
"""
import httplib2, ssl, sys

import tornado.ioloop
import tornado.web
import tornado.httpserver

import tornadio2.server

import hailingfrequency
from hailingfrequency import HailingFrequencyHandler, SocketIOHandler

import globals

class CanaryCall():
	def __init__(self, result=None):
		"""You may pass CanaryCall an object to set as its data (i.e. the result of a query).  If data is present, the result will automatically be set to 200 (OK)."""
		
		if result is not None:
			self.result = 200
			self.data = result.emit()
		else:
			self.result = 403
		
	def emit(self):
		"""Returns the CanaryCall object as a dict, which can be output as JSON"""
		return self.__dict__

class Users(tornado.web.RequestHandler):
	def get(self):
		"""GET: returns a list of all Users [according to optional criteria]."""
		
		canary_call = CanaryCall()
		self.write(canary_call.emit())
		
	def post(self):
		"""POST: creates a new User.
		
		Post data must contain a valid User object."""
		
		canary_call = CanaryCall()
		self.write(canary_call.emit())
		
class User(tornado.web.RequestHandler):
	def initialize(self, userId):
		self.userId = userId
		
	def get(self, userId):
		"""GET: returns the User matching specified id."""
		u = user.User()
		u.create()	
		
		canary_call = CanaryCall(result = u)
		self.write(canary_call.emit())
		
	def post(self, userId):
		"""POST: log in/out the User matching specified id."""
		
		canary_call = CanaryCall()
		self.write(canary_call.emit())
		
	def put(self, userId):
		"""PUT: updates the User's data."""
		
		canary_call = CanaryCall()
		self.write(canary_call.emit())
		
	def delete(self, nestId):
		"""DELETE: deletes the User."""
		
		canary_call = CanaryCall()
		self.write(canary_call.emit())
		
class Nests(tornado.web.RequestHandler):
	def get(self):
		"""GET: returns the Nests registered."""
		
		canary_call = CanaryCall()
		self.write(canary_call.emit())
		
	def post(self):
		"""POST: adds a new Nest.
		
		Post data must contain valid Nest object.
		"""
		
		canary_call = CanaryCall()
		self.write(canary_call.emit())
		
class Nest(tornado.web.RequestHandler):
	def initialize(self, nestId):
		self.nestId = nestId
		
	def get(self, nestId):
		"""GET: returns the Nest matching specified id."""
		
		canary_call = CanaryCall()
		self.write(canary_call.emit())
		
	def put(self, userId):
		"""PUT: updates the Nest's data."""
		
		canary_call = CanaryCall()
		self.write(canary_call.emit())
		
	def delete(self, nestId):
		"""DELETE: deletes the Nest."""
		
		canary_call = CanaryCall()
		self.write(canary_call.emit())
		
class Devices(tornado.web.RequestHandler):
	def get(self):
		"""GET: returns the Devices registered."""
		
		canary_call = CanaryCall()
		self.write(canary_call.emit())
		
	def post(self):
		"""POST: adds a new Device.
		
		Post data must contain valid Device object.
		"""
		
		canary_call = CanaryCall()
		self.write(canary_call.emit())
		
class Device(tornado.web.RequestHandler):
	def initialize(self, deviceId):
		self.deviceId = deviceId
		
	def get(self, deviceId):
		"""GET: returns the Device matching specified id."""
		print deviceId
		
		canary_call = CanaryCall()
		self.write(canary_call.emit())
		
	def put(self, deviceId):
		"""PUT: updates the Device's data."""
		
		canary_call = CanaryCall()
		self.write(canary_call.emit())
	
	def delete(self, deviceId):
		"""DELETE: deletes the Device."""
	
		canary_call = CanaryCall()
		self.write(canary_call.emit())
		
class Ping(tornado.web.RequestHandler):
	def initialize(self, entityId, action):
		self.entityId = entityId
		self.action = action
		
	def post(self, entityId, actionId):
		"""POST: sends a ping (event notification) to the specified entity, with action specified by the Action argument"""
		
		canary_call = CanaryCall()
		self.write(canary_call.emit())
		
class Status(tornado.web.RequestHandler):
	def initialize(self, entityId, status):
		self.entityId = entityId
		self.status = status
		
	def post(self, entityId, status):
		"""POST: gets the requested status from the specified entity"""
		
		canary_call = CanaryCall()
		self.write(canary_call.emit())
		
class Communicator(tornado.web.RequestHandler):
	def initialize(self, nestId):
		self.nestId = nestId
		
	def get(self, nestId):
		"""GET: gets the current communication session opened between members of a Nest, or null if uninitiated."""
		
		canary_call = CanaryCall()
		self.write(canary_call.emit())
		
	def post(self, nestId):
		"""POST: starts a new communication session between members of a Nest."""
		
		canary_call = CanaryCall()
		self.write(canary_call.emit())
		
	def delete(self, nestId):
		"""DELETE: ends the currently open communication session between members of a Nest."""
		
		canary_call = CanaryCall()
		self.write(canary_call.emit())
		
	def put(self, nestId):
		"""PUT: updates the currently open communication session between members of a Nest."""
		
		canary_call = CanaryCall()
		self.write(canary_call.emit())

api = tornado.web.Application([
	(r"/users/", Users),
	(r"/user/(.*)/", User, dict(userId = None)),
	(r"/nests/", Nests),
	(r"/nest/(.*)/", Nest, dict(nestId = None)),
	(r"/nest/(.*)/communicator/", Communicator, dict(nestId = None)),
	(r"/devices/", Devices),
	(r"/device/(.*)/", Device, dict(deviceId = None)),
	(r"/ping/(.*)/(.*)/", Ping, dict(entityId = None, action = None)),
	(r"/status/(.*)/(.*)/", Status, dict(entityId = None, status = None)),
	
	(r"/docs/(.*)", tornado.web.StaticFileHandler, {'path': globals.docs_path}),	# helpers; remove in production
	(r"/communicator/", HailingFrequencyHandler),
	(r"/js/socket.io.js", SocketIOHandler)
])

if __name__ == "__main__":
	from CanaryAssets.Device import Device as CanaryDevice
	from CanaryAssets.Nest import Nest as CanaryNest
	from CanaryAssets.User import User as CanaryUser	

	http_server = tornado.httpserver.HTTPServer(api)
	http_server.listen(5555)
	
	tornadio2.server.SocketServer(hailingfrequency.com, auto_start=False)
	
	tornado.ioloop.IOLoop.instance().start()