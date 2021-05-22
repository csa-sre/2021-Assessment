import socket
import threading


s = socket.socket()  # 创立套接字
host = '127.0.0.1'  # ip
port = 9088  # 端口
s.bind((host, port))  # 绑定
s.listen(5)
c, addr = s.accept()  # 连接


def rec(socket):
    while True:
        data1 = (socket.recv(2048)).decode('utf-8')
        print('收到来自客户端的消息:%s' % (data1))
        if len(data1) == 0:
            print('连接断开')
            socket.close()
            break


rec_a = threading.Thread(target=rec, args=(c, addr))
rec_a.start()

