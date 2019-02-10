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
    logger.debug('WebSockets listening on port 8888')
    tornado.ioloop.IOLoop.current().start()

def emit(message):
    WebSocketHandler.send_message(message)

class WebSocketHandler(tornado.websocket.WebSocketHandler):
    waiters = set()

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

    @classmethod
    def send_message(cls, message):
        logging.debug("Sending message to %d waiter(s)", len(cls.waiters))
        for waiter in cls.waiters:
            try:
                waiter.write_message(message)
            except:
                logging.error("Error sending message", exc_info=True)

    def on_message(self, message):
        if not message:
            return

        logger.debug(
            'Received WebSocket message from %s: %r',
            self.request.remote_ip, message)

        response = JSONRPCResponseManager.handle(
            message, dispatcher)

        WebSocketHandler.send_message(response.json)
