mport http.server, ssl

server_address = (‘0.0.0.0’, 8080)
httpd = http.server.HTTPServer(server_address, http.server.SimpleHTTPRequestHandler)
httpd.socket = ssl.wrap_socket(httpd.socket,
server_side=True,
certfile=’/home/arima/Documents/Firefox/localhost.pem’,
ssl_version=ssl.PROTOCOL_TLSv1_2)
httpd.serve_forever()
