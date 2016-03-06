import os
from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer
from threading import Thread

from germanium.static import *


def before_all(context):
    TCPServer.allow_reuse_address = True
    Handler = SimpleHTTPRequestHandler
    context._httpServer = TCPServer(("localhost", 8000), Handler)

    print("started server on localhost:8000")

    t = Thread(target=context._httpServer.serve_forever)
    t.start()

def after_all(context):
    context._httpServer.shutdown()

    reuse_browser = 'TEST_REUSE_BROWSER' in os.environ.keys()

    if reuse_browser:
        close_browser()

def after_scenario(context, scenario):
    keep_browser = 'TEST_KEEP_BROWSER' in os.environ.keys()
    reuse_browser = 'TEST_REUSE_BROWSER' in os.environ.keys()

    if keep_browser:
        print("Not closing the browser since TEST_KEEP_BROWSER is set")
    elif reuse_browser:
        print("Not closing the browser since TEST_REUSE_BROWSER is set")
    else:
        close_browser()
