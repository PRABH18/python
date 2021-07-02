import socket
ob=socket.socket()
ob.bind(('localhost',2301))
ob.listen(4)
clientobject,add=ob.accept()
print("server is ready to accept connection")
print('connected with this address',add)
gotmsg=clientobject.recv(1024)
