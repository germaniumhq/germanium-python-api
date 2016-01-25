import SimpleHTTPServer
import SocketServer
from threading import Thread

from behave import *

def before_all(context):
    Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
    context._httpServer = SocketServer.TCPServer(("localhost", 8000), Handler)

    t = Thread(target=context._httpServer.serve_forever)
    t.start()

def after_all(context):
    context._httpServer.shutdown()

def after_scenario(context, scenario):
    context.germanium.quit()

