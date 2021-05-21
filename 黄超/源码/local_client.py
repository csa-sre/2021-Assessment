import socket
import threading
def recv_msg(client):
	while True:
		data = client.recv(1024)	
		print('收到来自远程端口的数据:'+data.decode()) 
			
		
def send_msg(client):
	while True:
		try:
			message = input("请要发送的数据:")
			client.send(message.encode("utf-8"))    
			if message == 'quit':
				client.close()
				break
		except Exception as error:
			break
		
       
client =socket.socket()
host = '192.168.79.128'
port = 9922
print('输入quit结束程序')
client.connect((host,port))     #建立连接
t_recv = threading.Thread(target=recv_msg,args=(client,))
t_send = threading.Thread(target=send_msg,args=(client,))
t_recv.start()
t_send.start()