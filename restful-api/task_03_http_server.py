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
        self.send_response_only(200)
        # add condition for if endpoint is /data , /status and /
        if self.path == "/":
            send_response = "Hello, this is a simple API!"


if __name__ == "__main__":
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print("serving at port", PORT)
        httpd.serve_forever()