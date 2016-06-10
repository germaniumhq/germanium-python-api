import cgi
from http.server import SimpleHTTPRequestHandler

try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO


class PostHttpRequestHandler(SimpleHTTPRequestHandler):
    def do_POST(self):
        form = cgi.FieldStorage(
            fp= self.rfile,
            headers= self.headers,
            environ={'REQUEST_METHOD': 'POST',
                     'CONTENT_TYPE': self.headers['Content-Type'],
                     }
        )

        filename = form['file'].filename

        self.send_response(200)
        self.wfile.write(bytearray("<html><body>Uploaded '%s'.</body><html>" % filename, "utf-8"))
