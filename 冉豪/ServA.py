#服务端A

import socket
import time

#服务端A的地址及端口
hostA = '127.0.0.1'
portA = 3333  #此端口号与客户端一致
ServA_addr = (hostA, portA)
ServA_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
 
#服务端B的地址及端口
hostB = '127.0.0.1'
portB = 5555 #与服务端C的端口号相同
ServB_addr = (hostB, portB)

ServA_socket.bind(ServA_addr)  #将A套接字绑定到服务端A上，接收客户端的消息
ServA_socket.settimeout(100)  #设置time out 时间为100s

while True:
    try:
        now = time.time()
        datas , Clntaddr= ServA_socket.recvfrom(1024)
        print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
        print('服务端A:客户端 %s 发来信息：%s \n'%(Clntaddr, datas.decode('utf-8')))  #解码输出
        
        ServA_socket.sendto(datas, ServB_addr)  #转发给服务端B
        if datas == b'quit':  #传输quit时停止传输
            break
    except socket.timeout:
        print('time out!')  #停滞每一百秒提示一次time out

