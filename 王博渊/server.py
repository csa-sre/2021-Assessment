import socket
import threading


def replymessage(conn):
    while True:
        data = conn.recv(1024)
        conn.send(data)
        if data.decode().lower() == 'bye':
            break
    conn.close()


def main():
    sockscr = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sockscr.bind(('', port))
    sockscr.listen(200)
    only =input("请输入授权的的用户名")
    while True:
        try:
            conn, addr = sockscr.accept()
            if only != onlyYou:
                conn.close()
                continue
            t = threading.Thread(target=replymessage, args=(conn,))
            t.start()        
        except:
            print('error')


if __name__ == '__main__':
    try:
        port = input("请输入中间服务器端口")
        onlyYou = input("请设置允许访问的用户名")
        main()
    except:
        print('Must give me a number as port')
input("结束")
