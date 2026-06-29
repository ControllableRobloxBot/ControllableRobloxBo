from http.server import HTTPServer, BaseHTTPRequestHandler

Host = "192.168.0.182"
Port = 1679

class NeuralHTTP(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)

        # Send cookie to client
        self.send_header("Set-Cookie", "Data=10000000; Path=/")
        self.send_header("Content-type", "text/html")

        self.end_headers()
        self.wfile.write(b"Cookie set!")

    def do_POST(self):
        content_length = int(self.headers.get('Content-Length', 0))
        post_data = self.rfile.read(content_length)

        # Read cookie from request
        cookie = self.headers.get("Cookie")

        print("Cookie:", cookie)
        print("Received data:", post_data.decode("utf-8"))

        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()

        self.wfile.write(b'{"value":"10000000"}')

server = HTTPServer((Host, Port), NeuralHTTP)
print("Server started...")
server.serve_forever()