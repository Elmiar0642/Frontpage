mport http.server, ssl

server_address = (â0.0.0.0â, 8080)
httpd = http.server.HTTPServer(server_address, http.server.SimpleHTTPRequestHandler)
httpd.socket = ssl.wrap_socket(httpd.socket,
server_side=True,
certfile=â/home/arima/Documents/Firefox/localhost.pemâ,
ssl_version=ssl.PROTOCOL_TLSv1_2)
httpd.serve_forever()
