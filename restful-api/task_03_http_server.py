#!/usr/bin/python3
"""
Module task_03_http_server
"""
import http.server
import json


class Handler(http.server.BaseHTTPRequestHandler):
    """
    Setting up a basic HTTP server that responds to GET requests.
    """
    def do_GET(self):
        """
        Handles GET requests and responds based on the requested path.
        """
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        elif self.path == "/data":
            data = {"name": "John", "age": 30, "city": "New York"}
            to_json = json.dumps(data).encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(to_json)

        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")

        elif self.path == "/info":
            info = {"version": "1.0",
                    "description": "A simple API built with http.server"
                    }
            json_info = json.dumps(info).encode()
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json_info)

        else:
            self.send_response(404)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Endpoint not found")


if __name__ == "__main__":
    PORT = 8000
    server_address = ("", PORT)
    try:
        with http.server.HTTPServer(server_address, Handler) as httpd:
            print(f"Serving at port {PORT}: http://localhost:{PORT}")
            httpd.serve_forever()
    except KeyboardInterrupt:
        print("Server stopped.")
    except OSError as error:
        print(error)
