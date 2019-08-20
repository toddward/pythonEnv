from http.server import HTTPServer, BaseHTTPRequestHandler

from io import BytesIO

import os


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        # Send message back to client
        message = "Hello world!"
        message += os.environ['stuff']
        # Write content as utf-8 data
        self.wfile.write(bytes(message, "utf8"))

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        self.send_response(200)
        self.end_headers()
        response = BytesIO()
        response.write(b'This is POST request. ')
        response.write(b'Received: ')
        response.write(body)
        self.wfile.write(response.getvalue())


httpd = HTTPServer(('', 8080), SimpleHTTPRequestHandler)
httpd.serve_forever()
