from http.server import HTTPServer, SimpleHTTPRequestHandler
httpd = HTTPServer(('localhost', 8888), SimpleHTTPRequestHandler)
httpd.serve_forever()
