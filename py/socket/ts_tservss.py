from socketserver import (TCPServer as TCP, StreamRequestHandler as SRH)
from time import ctime

HOST = ''
PORT = 21567
ADDR = (HOST, PORT)


class MyRequestHandler(SRH):

    def __init__(self):
        pass

    def handle(self):
        print('...connected from:', self.client_address,
              self.wfile.write('[%s] %s' % (ctime(), self.rfile.readline())))

tcpServ = TCP(ADDR, MyRequestHandler)
print('wait for connection...')
tcpServ.serve_forever()
