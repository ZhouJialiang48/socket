from socket import *
from time import ctime

HOST = ''
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

while True:
    print('waiting for connection...')
    tcpCliSock, addr = tcpSerSock.accept()
    print('...connection from: {}'.format(addr))
    while True:
        data = tcpCliSock.recv(BUFSIZ).decode('utf8')
        if not data:
            break
        tcpCliSock.send('[{}] {}'.format(ctime(), data).encode('utf8'))
    tcpCliSock.close()
tcpCliSock.close()
