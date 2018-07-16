from socketserver import TCPServer as TCP
from socketserver import StreamRequestHandler as SRH
from time import ctime

HOST = ''
PORT = 21567
ADDR = (HOST, PORT)

class MyRequestsHandler(SRH):
    def handle(self):
        print('connected from: {}'.format(self.client_address))
        self.wfile.write('[{}] {}'.format(ctime(), self.rfile.readline().decode('utf8')).encode('utf8'))

tcpServ = TCP(ADDR, MyRequestsHandler)
print('waiting for connection...')
tcpServ.serve_forever()
