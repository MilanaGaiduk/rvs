import socket

serv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, proto=0)
serv_sock.bind(('192.168.249.130', 53211))
serv_sock.listen(10)
print('Server is listening')

f = open('numbers.txt', 'r')
f1 = open('database.txt','r')
k=1
ok = False

while True:
    # Бесконечно обрабатываем входящие подключения
    client_sock, client_addr = serv_sock.accept()
    print('Connected by', client_addr)

    while True:
        # Пока клиент не отключился, читаем передаваемые 
        # им данные и отправляем их обратно
        ok = False
        data = client_sock.recv(1024)
        if not data: 
            # Клиент отключился
            print('Connection closed')
            break

        id = data.decode()
        print("Client writes: ", id)

        with open('database.txt') as f1:
            for line in f1:
                if line[0]==id:
                    ok = True
                    answer = line[2:]
                    print(answer)
        if ok == False:
            answer = 'Error! This id does not exist in database'
        print("Sending to client: ", answer)
        answer = answer.encode()
        client_sock.send(answer)    
        if id == 'STOP':
            print('Connection closed')
            break
	
client_sock.close()
