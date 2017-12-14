import socket

serv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, proto=0)
serv_sock.bind(('192.168.249.130', 53210))
serv_sock.listen(10)
print('Server is listening')

f = open('numbers.txt', 'r')
k=1

while True:
    # Бесконечно обрабатываем входящие подключения
    client_sock, client_addr = serv_sock.accept()
    print('Connected by', client_addr)

    while True:
        # Пока клиент не отключился, читаем передаваемые 
        # им данные и отправляем их обратно
        data = client_sock.recv(1024)
        if not data: 
            # Клиент отключился
            print('Connection closed')
            break

        if (data==b'give me a number'):
            print("Client writes: ", data.decode())
            #print("k=",k)
            num = f.readline()
            print("Sending to client", num)
            num = num.encode()
            #k+=1

            client_sock.send(num)    
        #client_sock.sendall(data)
        #client_sock.send(b" 123")
	

client_sock.close()
