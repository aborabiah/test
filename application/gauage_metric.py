import http.server
from prometheus_client import start_http_server, Gauge
REQUEST_IN_PROGRESS = Gauge("app_requests_in_progress", "Number of requests currently being processed")

class HandleRequests(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        REQUEST_IN_PROGRESS.inc()
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        
        # Fixed HTML nesting: </h2> should come before </center>
        # Encoded the string to bytes directly
        message = "<html><head><title>First Python Application</title></head><body style='color: #333; margin-top: 30px;'><center><h2>Welcome to our first Python application.</h2></center></body></html>"
        
        self.wfile.write(bytes(message, "utf-8"))
        REQUEST_IN_PROGRESS.dec()
        # Removed self.wfile.close - let the server handle this!

if __name__ == "__main__":
    start_http_server(8001)
    # Changed to port 8000 to avoid conflicts on some systems
    server_address = ('0.0.0.0', 8000)
    httpd = http.server.HTTPServer(server_address, HandleRequests)
    
    print(f"Serving on http://{server_address[0]}:{server_address[1]} ...")
    httpd.serve_forever()