
from http.server import BaseHTTPRequestHandler, HTTPServer
import time, random

HOST = "localhost"
PORT = 8000

class ZenOfPythonServer(BaseHTTPRequestHandler):
    __ZenOfPython = [
        'Beautiful is better than ugly.',
        'Explicit is better than implicit.',
        'Simple is better than complex.',
        'Complex is better than complicated.',
        'Flat is better than nested.',
        'Sparse is better than dense..',
        'Readability counts.',
        'Special cases aren\'t special enough to break the rules.',
        'Although practicality beats purity.',
        'Errors should never pass silently.',
        'Unless explicitly silenced.',
        'In the face of ambiguity, refuse the temptation to guess.',
        'There should be one-- and preferably only one --obvious way to do it.',
        'Although that way may not be obvious at first unless you\'re Dutch.',
        'Now is better than never.',
        'Although never is often better than *right* now.',
        'If the implementation is hard to explain, it\'s a bad idea.',
        'If the implementation is easy to explain, it may be a good idea.',
        'Namespaces are one honking great idea -- let\'s do more of those!',
    ]

    @classmethod
    def __get_zen_of_python(cls):
        return random.choice(cls.__ZenOfPython)

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>ZenOfPython</title></head>", "utf-8"))
        self.wfile.write(bytes("<body><p>%s</p>" % self.__get_zen_of_python(), "utf-8"))


if __name__ == '__main__':

    myServer = HTTPServer((HOST, PORT), ZenOfPythonServer)
    print(time.asctime(), "Server Starts - %s:%s" % (HOST, PORT))

    try:
        myServer.serve_forever()
    except KeyboardInterrupt:
        pass

    myServer.server_close()
    print(time.asctime(), "Server Stops - %s:%s" % (HOST, PORT))
