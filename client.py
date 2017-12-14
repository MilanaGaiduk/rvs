import socket

client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_sock.connect(('192.168.249.130', 53210))

sum = 0
for i in range(5):
    client_sock.sendall(b'give me a number')
    data = client_sock.recv(1024)
    term = data.decode()
    sum += int(term)
    print('Received',term)
client_sock.close()
print('connection closed')
print('Sum = ', sum)
