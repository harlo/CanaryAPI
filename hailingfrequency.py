import tornado
import tornado.web
import tornado.httpserver

import tornadio2
import tornadio2.router
import tornadio2.conn


class HailingFrequencyHandler(tornado.web.RequestHandler):
	def get(self):
		self.render('index.html')
		
class SocketIOHandler(tornado.web.RequestHandler):
	def get(self):
		self.render('socket.io.js')
		
class HailingFrequency(tornadio2.conn.SocketConnection):
	participants = set()
	
	def on_open(self, info):
		self.send("HI")
		# TODO: if your cookie doesn't match your endpoint, get kicked out
		
		self.participants.add(self)
		
	def on_message(self, message):		
		for p in self.participants:			
			p.send(message)
			
	def on_close(self):
		self.participants.remove(self)
		
class Router(tornadio2.conn.SocketConnection):
	# TODO: get all nest ids...
	ep = ['/herpie','/derpie','/derpderp']
	__endpoints__ = {}
	for e in ep:
		__endpoints__[e] = HailingFrequency
		
hailing_frequency = tornadio2.router.TornadioRouter(Router)

com = tornado.web.Application(
	hailing_frequency.urls,
	socket_io_port = 5554
)