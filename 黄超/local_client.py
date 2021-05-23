import socket
import threading
import time
def recv_msg(client):
	global active
	while active:
		try:
			data = client.recv(1024)	
			data_str=str(data.decode('utf-8'))
			print('收到数据:%s' % ( data_str))
			if data_str=='quit':
				print('对方主动断开连接,终止连接' )
				client.close()
				active = False
				break 
			if len(data_str) == 0:
				print('对方断开了连接')
				client.close()
				active = False
				break
		except Exception as error:
			break
			
		
def send_msg(client):
	global active
	while active:
		try:
			message = input("请输入要发送的数据:")
			client.send(message.encode("utf-8"))    
			if message == 'quit':
				active = False
				client.close()
				break
			
		except Exception as error:
			break
		
active = True
active1 = True
i=0       
client =socket.socket()
host = '192.168.79.128'
port = 9922
print('输入quit结束程序')
while active1: #请求连接，每五秒发送一次，若一分钟后连接没有成功建立则终止程序
	try:
		client.connect((host,port))     #建立连接
		active1 = False
	except Exception as error:
		time.sleep(5)
		i=i+1
		if i==12:
			print('连接超时')
			active1=False
			active = False
		else:
			continue
t_recv = threading.Thread(target=recv_msg,args=(client,))
t_send = threading.Thread(target=send_msg,args=(client,))
t_recv.start()
t_send.start()
