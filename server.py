# File transfer server side

import socket

port = 22882
sock = socket.socket()
host = socket.gethostname()
sock.bind((host,port))
sock.listen(5)

print 'Server Ready...'

while True:
        conn, addr = sock.accept()
        print 'Connected from', addr
        data = conn.recv(1024)
        print ('Data received from client', repr(data))

        fl='penecontetas.png'
        f = open(fl,'rb')
        payload = f.read(1024)
        while(payload):
                conn.send(payload)
                print('Sending data...', repr(payload))
                payload = f.read(1024)
        f.close()

        print ('Transmission done by the server')
        conn.send('Fuck you')
        conn.close()
