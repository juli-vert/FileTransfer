# File Transfer client side
'''
v09072016.0
Version with single thread client
Client always waiting to receive data from the server
'''

import socket

# open a socket connected to the server port
sock = socket.socket()
host = "192.168.1.34" #if the client is not running on the same server change the ip address
port = 22882

host = input("Enter the ip address of the server that you wanna connect to: ")
port = int(input("Enter the port of the server: "))

fpath = "C:\\Users\\Pere\\Desktop\\FileTransfer\\received\\" # path to the folder where the files will be placed

bsize = 1024	
# request for the directory
sock.connect((host,port))

flcount = 0
print ('Waiting for data...')

while True:
	data = sock.recv(bsize)
	if "Sending file" in data.decode():
		ext = '.{0}'.format(data.decode().rsplit('.',1)[1])
		flname = '{0}{1}{2}{3}'.format(fpath,"newfile",str(flcount),ext)
		with open(flname,'wb') as f:
			print ('Getting new file...')
			sock.send("ok".encode())
			data = sock.recv(bsize)
			while data:
				if "eof" in data.decode("utf-8", "replace"):
					break
				else:
					f.write(data)
					sock.send("ok".encode())
					data = sock.recv(bsize)
		f.close()
		flcount = flcount + 1
