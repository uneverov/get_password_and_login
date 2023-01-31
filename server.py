from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import unquote

host_name = "194.58.107.248"
server_port = 20

class MyServer(BaseHTTPRequestHandler):
    chat_text = []
    def do_POST(self):
        login = unquote(self.path, encoding='utf-8').split('&')[0].replace('login=', '').replace('/?', '')
        message = unquote(self.path, encoding='utf-8').split('&')[1].replace('message=', '')
        self.chat_text.append(f'> {login}: {message}\n')
        self.send_response(200)
        self.end_headers()

    def do_GET(self):
        self.send_response(200)
        x = ''.join(self.chat_text)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        my_str_as_bytes = str.encode(x)
        self.wfile.write(my_str_as_bytes)

if __name__ == "__main__":
    webServer = HTTPServer((host_name, server_port), MyServer)
    print("Server started http://%s:%s" % (host_name, server_port))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")