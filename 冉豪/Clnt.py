#基于UDP的数据转发
#客户端发送给到服务端A，服务端A转发到服务端B,输入'quit'时停止
#本地转发

#客户端

import socket
import time

host = '127.0.0.1'  #本地地址
port = 3333  #连接服务端A的端口号
Clnt_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  #创建基于UDP的套接字
ServA_addr = (host, port)

while True:
    start = time.time() #标记开始时间
    print(time.strftime('%Y-%m%d %H:%M:%S', time.localtime(start)))  #输出当前时间
    datas = input('请输入传输内容：')
    Clnt_socket.sendto(datas.encode('utf-8'), ServA_addr)  #转为二进制编码形式发送数据
    now = time.time()
    run_time = (now - start)/100.0  #运行时间
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(now)))
    print('run_time：%f seconds \n'%run_time)
    if datas == 'quit':
        break   #输入quit是停止

