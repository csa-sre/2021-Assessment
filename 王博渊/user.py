import socket


def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((ip, port))
    while True:
        data = input("请输入目标服务器IP")
        sock.send(data.encode())
        print(sock.recv(1024).decode())
        if data.lower() == 'bye':
            break
    sock.close()


if __name__ == '__main__':
    try:
        ip = input("输入中间服务器的IP")
        port = input("输入中间服务器的端口")
        main()
    except:
        print('error')
input("结束")
