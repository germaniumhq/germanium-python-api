from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer
from threading import Thread
import os

from behave import *

def before_all(context):
    TCPServer.allow_reuse_address = True
    Handler = SimpleHTTPRequestHandler
    context._httpServer = TCPServer(("localhost", 8000), Handler)

    t = Thread(target=context._httpServer.serve_forever)
    t.start()

def after_all(context):
    context._httpServer.shutdown()

def after_scenario(context, scenario):
    if 'TEST_KEEP_BROWSER' not in os.environ.keys():
        context.germanium.quit()
    else:
        print("Not closing the browser since TEST_KEEP_BROWSER is set")

