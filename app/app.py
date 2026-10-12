
from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import os


class CloudAIHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == "/health":
            response = {
                "status": "healthy",
                "application": "Cloud AI DevOps Platform"
            }
        elif self.path == "/":
            response = {
                "message": "Welcome to Cloud AI DevOps Platform!",
                "version": "1.0.0",
                "status": "running"
            }
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'{"error": "Not Found"}')
            return

        body = json.dumps(response).encode("utf-8")

        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)


port = int(os.environ.get("PORT", "8000"))
server = HTTPServer(("0.0.0.0", port), CloudAIHandler)

print(f"Cloud AI DevOps Platform running on port {port}")

server.serve_forever()