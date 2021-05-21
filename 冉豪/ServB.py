#服务端B

import socket
import time

#服务端B的地址及端口
hostB = '127.0.0.1'
portB = 5555
ServB_addr = (hostB, portB)
ServB_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
ServB_socket.bind(ServB_addr)  #将B套接字绑定到服务端B上,接收A的消息


while True:
    now = time.time()
    datas , ServA_addr = ServB_socket.recvfrom(1024)
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
    print('服务端B:服务端A %s 发来信息：%s  \n'%(ServA_addr, datas.decode('utf-7')))  #解码输出

    if datas == b'quit':  #传输quit时停止传输
         break

