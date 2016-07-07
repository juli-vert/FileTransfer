# File Transfer client side

import socket

# open a socket connected to the server port
sock = socket.socket()
host = "192.168.1.34" #if the client is not running on the same server change the ip address
port = 22882

host = input("Enter the ip address of the server that you wanna connect to: ")
port = int(input("Enter the port of the server: "))

bsize = 1024	
# request for the directory
sock.connect((host,port))
sock.send("which files do you have for me?".encode())


dirs = sock.recv(bsize)
print (dirs.decode())

# select the file and send the choice to the server
opt = input("Select which file you want to download\n")
sock.send(opt.encode())

# get the data
with open('rfile2', 'wb') as f:
    print ('Opening file...')
    while True:
        print ('Getting new data...')
        data = sock.recv(bsize)
        print('data=%s', (data))
        if not data:
                break
        f.write(data)

# close the connection
f.close()
print('Transfer done')
sock.close()
print ('Closing...')