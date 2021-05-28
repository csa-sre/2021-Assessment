import socket
import threading


s = socket.socket()  # 创立套接字
host = '192.168.43.1'  # ip
port = 9088  # 端口
s.bind((host, port))  # 绑定
s.listen(5)
c, addr = s.accept()  # 连接


def sen(s):
    while True:
        try:
            data1 = input("请输入要发送的信息：")
            data1 = (s.send(2048)).encode('UTF-8')
        except Exception as error:
            print('发送失败', error)
            s.close()
            break


def rec(s):
    while True:
        data2 = (s.recv(2048)).decode('utf-8')
        print('收到来自客户端的消息:%s' % (data2))
        if len(data2) == 0:
            print('连接断开')
            s.close()
            break


rec_a = threading.Thread(target=rec, args=(c, addr))
sen_a = threading.Thread(target=sen, args=(c, addr))
rec_a.start()
sen_a.start()
