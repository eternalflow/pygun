import os
import sys
from collections import OrderedDict
from functools import partial

from gevent.pywsgi import WSGIHandler
from geventwebsocket import WebSocketApplication, WebSocketServer, Resource
from gundb.geventserver import GeventGunServer


HOST = os.getenv('HOST', '0.0.0.0').strip()
PORT = int(os.getenv('PORT', '8080').strip())


if __name__ == "__main__":
    GeventGunServer.backend = sys.argv[1]
    server = WebSocketServer(
        (HOST, PORT),
        Resource(OrderedDict([
            ('/gun', GeventGunServer),
        ])))
    print("started..")
    server.serve_forever()
