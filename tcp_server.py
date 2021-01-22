import socket

def filefn(csession,addr):
	z=csession.recv(1024)
	print("Client: {0}".format(z))
	if "file" in z:
		csession.send(b"Name the file below this")
		y=csession.recv(1024)
		filesend(csession,addr,y)
	print("Server:")
	x=str(raw_input())
	csession.send(b"{0}".format(x))


def filest(csession,addr):
	z=csession.recv(1024)
	print(z)
	csession.send(b"Hi! This is server.")


def filesend(csession,addr,name):
	f=open(name,'rb')
	l=f.read(1024)
	while(l):
		csession.send(l)
		print("sent",repr(l))
		l=f.read(1024)
	f.close()
	print('Done sending')


s=socket.socket()
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
ip=""
port=2222
s.bind( (ip,port) )
s.listen(2222)
csession,addr=s.accept()
print("Waiting for connection...")
print("Connection established with {0}:Server".format(addr))
filest(csession,addr)
while True:
	s.listen(2222)
	filefn(csession,addr)
