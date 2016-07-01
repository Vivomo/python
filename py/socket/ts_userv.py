from socket import *
from time import ctime

HOST = ''
PORT = 21567
BUFSIZ = 2014

ADDR = (HOST, PORT)

udpSerSock = socket(AF_INET, SOCK_DGRAM)
udpSerSock.bind(ADDR)

while True:
    print('wait for message...')
    data, addr = udpSerSock.recvfrom(BUFSIZ)
    send_data = '[%s] %s' % (bytes(ctime(), 'utf-8'), data)

    udpSerSock.sendto(send_data.encode(), addr)
    print('...received from and returned to:', addr)

udpSerSock.close()
