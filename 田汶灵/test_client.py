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


to_a = threading.Thread(target=to, args=(c,))
to_a.start()


