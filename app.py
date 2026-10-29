from http.server import HTTPServer, BaseHTTPRequestHandler

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"<h1>Hello from Docker!</h1>")

server = HTTPServer(("0.0.0.0", 8080), MyHandler)
print("Application running on port 8080")
server.serve_forever()
