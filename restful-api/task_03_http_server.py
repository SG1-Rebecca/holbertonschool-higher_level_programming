#!/usr/bin/python3
"""
Module to set up a simple HTTP server.
"""

import http.server
import socketserver
import json

PORT = 8000

class Handler(http.server.BaseHTTPRequestHandler):
    """

    """
    def do_GET(self):
        """
        """
        # add condition for if endpoint is /data , /status and /
        if self.path == "/":
            self.send_response_only(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!\n")

if __name__ == "__main__":
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print("serving at port", PORT)
        httpd.serve_forever()