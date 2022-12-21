from http.server import HTTPServer,BaseHTTPRequestHandler

content ="""
<html>
<body>
<h1>Top 3 Programming Languages</h1>
<h3>Python</h3>
<h3>C Programming</h3>
<h3>L Programming</h3>
</body>
</html>
"""

class WebHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('content-type','text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
    
server_address=('',8080)
httpd=HTTPServer(server_address,WebHandler)
print("Web server running...")
httpd.serve_forever()