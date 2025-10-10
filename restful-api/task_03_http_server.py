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
    Custon HTTP request handler.
    """
    def do_GET(self):
        """
        Handles GET requests based on different endpoints.
        """
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!\n")

        elif self.path == "/data":
            error = {"name": "John", "age": 30, "city": "New York"}
            json_data = json.dumps(error).encode("utf-8")
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json_data)

        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")

        elif self.path == "/info":
            info = {"version": "1.0", "description": "A simple API built with http.server"}
            json_info = json.dumps(info).encode()
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json_info)

        else:
            self.send_response(404)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(b"Endpoint not found")



if __name__ == "__main__":
    try:
        with socketserver.TCPServer(("", PORT), Handler) as httpd:
            print(f"Serving at port {PORT}: http://localhost:{PORT}")
            httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped.")
    except OSError as error:
        print(error)
