import socket #导入模块
import threading
def recv_msg(socket,addr):
	while True:
		data = socket.recv(1024)     #接受服务端发送的信息
		data_str=str(data.decode('utf-8'))
		print('受到数据:%s' % ( data_str))
		if data_str=='quit':
			print('对方主动断开连接,终止连接' )
			socket.close()
			break
def send_msg(socket,addr):
	while True:	
		try:
			res_data = input('请输入要发送的数据:')
			socket.send(res_data.encode('UTF-8'))      # send byte data
		except Exception as error:
			print('send_send_send_', error)
			socket.close()
			break
			


server = socket.socket()    #建立一个服务端
host = '127.0.0.1'   #获取主机ip地址
port = 9921    #设置端口
server.bind((host,port))    #绑定端口
server.listen(5)     #等待连接
c,addr = server.accept()     #建立连接

t_recv = threading.Thread(target=recv_msg,args=(c,addr))
t_send = threading.Thread(target=send_msg,args=(c,addr))
t_send.start()
t_recv.start()
#c.close()