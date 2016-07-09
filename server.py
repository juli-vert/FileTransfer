# File transfer server side
'''
v09072016.0
Version with server multithreading
Allows massive transfer from a specific folder in the server side to another folder in the client
New files can be added to the source folder (refeed) 
'''

import socket
import os, sys
import threading
import time
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
            print ("waiting for connections...")
            (conn, (ip,port)) = self.sock.accept()
            conn.settimeout(360)

            threading.Thread(target = ServerThread, args = (conn,ip,port)).start()

            '''if input() == "q":
                break'''

class ServerThread(object):
    
    def __init__(self,conn,ip,port):
        self.ip = ip
        self.port = port
        print ('{0}-{1}:{2}'.format("New client connected",str(ip),str(port)))
        self.runThread(conn,'{0}:{1}'.format(str(ip),str(port)))

    def runThread(self,conn,addr):
        while True:
            #print  ('Connected from', addr)
            #data = conn.recv(bsize)
            #print ('Data received from client', repr(data.decode()))

            dirs = os.listdir(fpath)
            time.sleep(10)
            for fl in dirs:
                msg = '{0}{1}'.format("Sending file: ",fl)
                conn.send(msg.encode())
                if "ok" in conn.recv(bsize).decode(): # client ready to receive
                    selfl = '{0}{1}'.format(fpath,fl)
                    f = open(selfl,'rb')
                    payload = f.read(bsize)

                    while (payload):
                        conn.send(payload)
                        print('........')
                        if "ok" in conn.recv(bsize).decode():
                            payload = f.read(bsize)
                    conn.send("eof".encode())
                    f.close()
                    # once the file is sent, it must be removed
                    os.remove(selfl)

# main program
host = input("Enter your ip address: ")
port = input("Enter the port that you wanna use for the server: ")
srv = mainServer(host,int(port))

