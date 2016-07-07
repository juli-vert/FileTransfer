# File transfer server side

import socket
import os, sys

# create socket listening on the port 22882
port = 22882
sock = socket.socket()
host = socket.gethostname()
sock.bind((host,port))
sock.listen(5)

# path to the folder where the files are placed
fpath = "C:\\Users\\Pere\\Desktop\\FileTransfer\\files\\"

print ('Server Ready...')

# loop to get a connection
while True:
    conn, addr = sock.accept()
    print  ('Connected from', addr)
    data = conn.recv(1024)
    print ('Data received from client', repr(data))

    dirs = os.listdir(fpath)

    print (len(dirs))
    ldir = dirs[0]
    for i in range(1,len(dirs)):
        ldir = '{0}{1}{2}'.format(ldir,"\n",dirs[i])

    print (ldir)
    conn.send(ldir.encode())

    print ("File selected")
    fl = '{0}{1}'.format(fpath,conn.recv(1024).decode())

    # open the selected file and send the data across
    f = open(fl,'rb')
    payload = f.read(1024)
    while(payload):
        conn.send(payload)
        print('Sending data...', repr(payload))
        payload = f.read(1024)
    f.close()

    # end the session
    print ('Transmission done by the server')
    conn.send(b'Fuck you')
    conn.close()
    break