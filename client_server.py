import socket
ob=socket.socket()
ob.connect(('localhost',2301))
msg='hello this is first client'
ob.send(msg.encode('utf-8'))


