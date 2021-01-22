import socket

def filefn(s):
    print("Client:")
    z=str(input())
    s.send("{0}".format(z).encode())
    if "file" in z:
      y=s.recv(1024)
      print(y)
      a=str(input())
      s.send("{0}".format(a).encode())
      filerecv(s,a)
    print("Server:")
    x=s.recv(1024)
    print(x)
    


def filest(s):
  s.send(b"Hi! This is client.")
  print("Server:")
  z=s.recv(1024)
  print(z)
  

def filerecv(s,a):
  i=0
  with open(a,'wb') as f:
    print("file opened")
    while i==0:
      print('receiving data...')
      data=s.recv(1024)
      print('data=%s',(data))
      i=1
      f.write(data)
  f.close()
  print("file transferred successful")
 



s=socket.socket()
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ip="13.126.237.194"
port=2222
s.connect( (ip,port) )
filest(s)
while True:
    filefn(s)
    


