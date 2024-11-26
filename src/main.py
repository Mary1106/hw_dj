from http.server import BaseHTTPRequestHandler, HTTPServer
from config import file_contact_html

hostName = "localhost"
serverPort = 8080


class MyServer(BaseHTTPRequestHandler):
    """Класс, отвечающий за обработку входящих запросов"""
    def do_GET(self):
        """Метод для обработки GET-запросов"""
        self.send_response(200)  # Отправка кода ответа
        self.send_header("Content-type", "text/html")
        self.end_headers()
        with open(file_contact_html, encoding='utf-8') as f:
            content = f.read()
        self.wfile.write(bytes(content, "utf-8"))

    def do_POST(self):
        content_length = int(self.headers["Content-Length"])
        post_data = self.rfile.read(content_length)
        print(post_data)

        response = f"Received POST data: {post_data.decode('utf-8')}"
        print(response)

if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
