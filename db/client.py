import socket

client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_sock.connect(('192.168.249.130', 53210))

f1 = open('cldb.txt','r')

a=''
flag=True
print('Write STOP to stop interacting')
while a!= 'STOP':
    print("Write id")
    a = input()
    client_sock.sendall(a.encode())
    data = client_sock.recv(1024)
    name = data.decode()
    print('Received: ',name)
    if name=='Error! This id does not exist in database':
        flag=False
    with open('cldb.txt') as f1:
            for line in f1:
                if line[0]==a:
                    answer = line[2:]
    if flag:
        print(name+" works on project "+ answer)
    flag=True
	
client_sock.close()
print('Connection closed')

