from threading import Thread
from http.server import BaseHTTPRequestHandler, HTTPServer

def run_dummy_server():
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"Bot is running")

    server = HTTPServer(('0.0.0.0', 8080), Handler)
    server.serve_forever()

Thread(target=run_dummy_server, daemon=True).start()
