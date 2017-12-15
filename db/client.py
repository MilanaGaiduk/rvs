import socket

client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_sock.connect(('192.168.249.130', 53210))

a=''
print('Write STOP to stop interacting')
while a!= 'STOP':
    print("Write id")
    a = input()
    client_sock.sendall(a.encode())
    data = client_sock.recv(1024)
    term = data.decode()
    print('Received: ',term)
client_sock.close()
print('Connection closed')

