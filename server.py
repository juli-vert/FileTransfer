# File transfer server side

import socket
import os, sys

port = 22882
sock = socket.socket()
host = socket.gethostname()
sock.bind((host,port))
sock.listen(5)

print ('Server Ready...')

while True:
    conn, addr = sock.accept()
    print  ('Connected from', addr)
    data = conn.recv(1024)
    print ('Data received from client', repr(data))

    dirs = os.listdir("C:\\Users\\Pere\\Desktop\\FileTransfer\\files")

    print (len(dirs))
    ldir = dirs[0]
    for i in range(1,len(dirs)):
        ldir = '{0}{1}{2}'.format(ldir,"\n",dirs[i])

    print (ldir)
    conn.send(ldir.encode())

    print ("File selected")
    fl = '{0}{1}'.format("C:\\Users\\Pere\\Desktop\\FileTransfer\\files\\",conn.recv(1024).decode())

    f = open(fl,'rb')
    payload = f.read(1024)
    while(payload):
        conn.send(payload)
        print('Sending data...', repr(payload))
        payload = f.read(1024)
    f.close()

    print ('Transmission done by the server')
    conn.send(b'Fuck you')
    conn.close()
    break