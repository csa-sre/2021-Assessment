import socket
import threading


def middle(conn, addr):
    sockdst = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sockdst.connect((ipServer,portServer))
    while True:
        data = conn.recv(1024).decode()
        print("收到客户端消息："+data)
        if data == "不要发给服务器":
            conn.send("该消息已被代理服务器过滤".encode())
            print("该消息已过滤")
        elif data.lower() == 'bye':
            print(str(addr)+"客户端关闭连接")
            break
        else:
            sockdst.send(data.encode())
            print("已转发服务器")
            data_fromserver = sockdst.recv(1024).decode()
            print("收到服务器回复的消息："+data_fromserver)
            if data_fromserver == '不要发给客户端':
                conn.send("该消息已被代理服务器修改".encode())
                print("消息已改变")
            else:
                conn.send(b'Server reply:'+data_fromserver.encode())
                print("已转发服务器消息给客户端")
        
    conn.close()
    sockdst.close()


def main():
    sockscr = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sockscr.bind(('', portScr))
    sockscr.listen(200)
    print("代理已启动")
    while True:
        try:
            conn, addr = sockscr.accept()
            t = threading.Thread(target=middle, args=(conn, addr))
            t.start()
            print("新用户："+str(addr))
        except:
            pass


if __name__ == '__main__':
    try:
        portScr = input("输入开放的的中间服务器端口")
        ipServer = input("输入目标服务器IP")
        portServer = input("输入目标服务器端口")
        main()
    except:
        print('Sth error')
input("结束")
