import socket
import time


if __name__ == '__main__':
    count_read = 512
    ip = 'localhost'
    port = 123

    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        sock.connect((ip, port))

        while True:
            request = input('Введите запрос или exit для выхода: ')
            sock.send(request.encode())

            if request.lower() == 'exit':
                break

            print('Время: ' + time.ctime(float(sock.recv(count_read).decode())))
