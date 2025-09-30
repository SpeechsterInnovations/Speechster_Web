import http.server
import socketserver

# Defining PORT number
PORT = 8980

# Creating handle
Handler = http.server.SimpleHTTPRequestHandler

# Creating TCPServer
http = socketserver.TCPServer(("", PORT), Handler)

# Getting logs
print("Serving at port:", PORT)
http.serve_forever()
