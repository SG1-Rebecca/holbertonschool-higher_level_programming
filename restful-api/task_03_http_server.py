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
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!\n")

        elif self.path == "/data":
            data = {"name": "John", "age": 30, "city": "New York"}
            json_data = json.dumps(data).encode("utf-8")
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json_data)

if __name__ == "__main__":
    try:
        with socketserver.TCPServer(("", PORT), Handler) as httpd:
            print("serving at port", PORT)
            httpd.serve_forever()
    except KeyboardInterrupt:
        print("Server stopped.")