import socket
import threading


c = socket.socket()
host = "127.0.0.1"
port = 9077
print('如果想终止程序，请直接回车')
c.connect((host, port))


def to(c):
    while True:
        try:
            data = input("请输入要发送的数据:")
            c.send(data.encode("utf-8"))
            if len(data) == 0:
                c.close()
                break
        except Exception as e:
            break


def rec(c):
    while True:
        data1 = (c.recv(2048)).decode('utf-8')
        print('收到来自服务端的消息:%s' % (data1))
        if len(data1) == 0:
            print('连接断开')
            c.close()
            break


to_a = threading.Thread(target=to, args=(c,))
rec_a = threading.Thread(target=rec, args=(c,))
to_a.start()
rec_a.start()


