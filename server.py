# File transfer server side

import socket
import os, sys
import threading
#import SocketServer

# Main variables and constants
port = 22882
host = "192.168.1.34" # local IP address of my computer
fpath = "C:\\Users\\Pere\\Desktop\\FileTransfer\\files\\" # path to the folder where the files are placed
bsize = 1024

class mainServer(object):

    def __init__(self,host,port):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        #host = socket.gethostname()
        self.sock.bind((host,port))
        self.sock.listen(5)
        print ('Server Ready...')
        self.runServer()

    def runServer(self):
        # loop to get a connection
        while True:
            (conn, (ip,port)) = self.sock.accept()
            conn.settimeout(360)

            threading.Thread(target = ServerThread, args = (conn,ip,port)).start()
            '''thr = ServerThread(ip,port)
            thr.runServer(str(ip)+str(port))'''

            if input():
                break

class ServerThread(object):
    
    def __init__(self,conn,ip,port):
        self.ip = ip
        self.port = port
        print ('{0}-{1}:{2}'.format("New client connected",str(ip),str(port)))
        self.runThread(conn,str(ip)+str(port))

    def runThread(self,conn,addr):
        while True:
            print  ('Connected from', addr)
            data = conn.recv(bsize)
            print ('Data received from client', repr(data))

            dirs = os.listdir(fpath)

            print (len(dirs))
            ldir = dirs[0]
            for i in range(1,len(dirs)):
                ldir = '{0}{1}{2}'.format(ldir,"\n",dirs[i])

            print (ldir)
            conn.send(ldir.encode())

            print ("File selected")
            fl = '{0}{1}'.format(fpath,conn.recv(bsize).decode())

            # open the selected file and send the data across
            f = open(fl,'rb')
            payload = f.read(bsize)
            while(payload):
                conn.send(payload)
                print('Sending data...', repr(payload))
                payload = f.read(bsize)
            f.close()

            # end the session
            print ('Transmission done by the server')
            conn.send(b'Fuck you')
            conn.close()
            break  


srv = mainServer(host,port)

