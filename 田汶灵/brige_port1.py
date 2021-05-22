import socket
import threading


s_host = "127.0.0.1"
s_port = 9077
c_host = "127.0.0.1"
c_port = 9088


# 将来自s套接字的数据转发到c套接字
def fw(s, c):
    try:
        while True:
            buf = s.recv(4096)
            print("{} ====> {} {} 字节".format(s.getpeername(), c.getpeername(), len(buf)))
            if (len(buf) == 0):
                print("{} 断开连接".format(s.getpeername()))
                return
            c.send(buf)
    except:
        return


# 处理请求，每一个连接对应一个
def rt(request_socket):
    des_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        des_socket.connect((c_host, int(c_port)))
    except Exception as e:
        print("连接目标 {}:{} 失败！error: {}".format(c_host, c_port, str(e)))
    threading.Thread(target=fw, args=(request_socket, des_socket)).start()
    fw(des_socket, request_socket)


if s_host == "127.0.0.1":
    print("将会监听: 127.0.0.1")
if s_port == 0 or c_port == 0:
    print("没有指定端口号或指定为0")

print("监听 {}:{}".format(s_host, s_port))
print("将会连接 {}:{}".format(c_host, c_port))

s_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 创建套接字
try:
    s_socket.bind((s_host, int(s_port)))
except Exception as e:
    print("绑定 {}:{} 端口失败 {}".format(s_host, s_port, str(e)))
s_socket.listen(50)  # 允许最大连接数
print("万事俱备")
while True:
    r_socket, addr = s_socket.accept()
    print("{} 已连接".format(r_socket.getpeername()))
    threading.Thread(target=rt, args=(r_socket,)).start()