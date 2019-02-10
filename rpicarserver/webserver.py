import logging
import tornado.ioloop
import tornado.web
import tornado.websocket

from jsonrpc import JSONRPCResponseManager, dispatcher

logger = logging.getLogger(__name__)

def start():
    app = tornado.web.Application([
        (r"/", WebSocketHandler),
    ], debug = True)
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()

class WebSocketHandler(tornado.websocket.WebSocketHandler):
    def open(self):
        logger.debug(
            'New WebSocket connection from %s',
            self.request.remote_ip)

    def check_origin(self, origin):
        return True

    def on_close(self):
        logger.debug(
            'Closed WebSocket connection from %s',
            self.request.remote_ip)

    def on_message(self, message):
        if not message:
            return

        logger.debug(
            'Received WebSocket message from %s: %r',
            self.request.remote_ip, message)

        response = JSONRPCResponseManager.handle(
            message, dispatcher)

        self.write_message(response.json)
