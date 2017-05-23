from http.server import HTTPServer, BaseHTTPRequestHandler
import io
import shutil
import urllib


class MyHttpHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        name = "World"
        if '?' in self.path:  # 如果带有参数
            self.queryString = urllib.parse.unquote(self.path.split('?', 1)[1])
            params = urllib.parse.parse_qs(self.queryString)
            print(params)
            name = params["name"][0] if "name" in params else None

        r_str = "Hello " + name + " <form action='' method='POSt'>Name:<input name='name' /><br /><input type='submit' value='submit' /></form>"
        enc = "UTF-8"
        encoded = ''.join(r_str).encode(enc)
        f = io.BytesIO()
        f.write(encoded)
        f.seek(0)
        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=%s" % enc)
        self.send_header("Content-Length", str(len(encoded)))
        self.end_headers()
        shutil.copyfileobj(f, self.wfile)

    def do_POST(self):
        s = str(self.rfile.readline(), 'UTF-8')  # 先解码
        print(urllib.parse.parse_qs(urllib.parse.unquote(s)))  # 解释参数
        self.send_response(301)  # URL跳转
        self.send_header("Location", "/?" + s)
        self.end_headers()


httpd = HTTPServer(('', 8080), MyHttpHandler)
print("Server started on 127.0.0.1,port 8080.....")
httpd.serve_forever()
