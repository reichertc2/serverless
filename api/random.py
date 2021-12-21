from http.server import BaseHTTPRequestHandler
import random
from urllib import parse


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        s = self.path
        url_components = parse.urlsplit(s)
        query_string_list = parse.parse_qsl(url_components.query)
        num = int(query_string_list)
        if num < 0 or num==None:
            random_number = "not positive, think positive"
        random_number = random.randrange(0, num)

        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        message = str(f"Your random number is {random_number}")
        self.wfile.write(message.encode())
