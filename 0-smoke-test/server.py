import logging
import socketserver

logging.basicConfig(
    format="%(asctime)s %(levelname)-8s %(message)s",
    level=logging.INFO,
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger()

HOST = "0.0.0.0"
PORT = 1024


class EchoServer(socketserver.BaseRequestHandler):
    def handle(self):
        while data := self.request.recv(1024):
            logger.info("%s wrote: %r", self.client_address[0], repr(data))
            self.request.sendall(data)
        self.request.close()


if __name__ == "__main__":
    with socketserver.TCPServer((HOST, PORT), EchoServer) as server:
        logger.info("online - serving from %s:%s", HOST, PORT)
        server.serve_forever()
