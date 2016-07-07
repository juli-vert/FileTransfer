# File Transfer client side

import socket

sock = socket.socket()
host = socket.gethostname()
port = 22882

sock.connect((host,port))
sock.send("connecting...")

with open('rfile', 'wb') as f:
        print 'Opening file...'
        while True:
                print 'Getting new data...'
                data = sock.recv(1024)
                print('data=%s', (data))
                if not data:
                        break
                f.write(data)
f.close()
print('Transfer done')
sock.close()
print 'Closing...'