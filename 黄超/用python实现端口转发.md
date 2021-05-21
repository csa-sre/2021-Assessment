#用python实现简单的端口转发
#端口转发源码
	import socket
    import threading
    def tcp_mapping_worker(conn_receiver, conn_sender):
    	while True:
    		try:
    			data = conn_receiver.recv(2048)
    			except Exception:
    			print('Event: Connection closed.')
    			break
	    
	        if not data:
	            print('Info: No more data is received.')
	            break
	    
	        try:
	            conn_sender.sendall(data)
	        except Exception:
	            print('Error: Failed sending data.')
	            break
	    
	        print('Info: Mapping > %s -> %s > %d bytes.' % (conn_receiver.getpeername(), conn_sender.getpeername(), len(data)))
	    
	    conn_receiver.close()
	    conn_sender.close()
	    
	    return

    s = socket.socket()
  
    local_host = '192.168.79.128'
    local_port = 9922
    
    remote_host = '127.0.0.1'
    remote_port = 9921
    
    s.bind((local_host,local_port))
    print('本机ip地址和端口'+local_host+':'+str(local_port))
    print('远端ip地址和端口'+remote_host+':'+str(remote_port))
    s.listen(5)
    
    print('Starting mapping service on ' + local_host+ ':' + str(local_port) + ' ...')
    c,addr = s.accept()
    s2=socket.socket()
    
    s2.connect((remote_host, remote_port))
    
    threading.Thread(target=tcp_mapping_worker,args=(c,s2)).start() 
    threading.Thread(target=tcp_mapping_worker,args=(s2,c)).start()

#本地端口客户端源码
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
    client.connect((host,port)) #建立连接
    t_recv = threading.Thread(target=recv_msg,args=(client,))
    t_send = threading.Thread(target=send_msg,args=(client,))
    t_recv.start()
    t_send.start()
#远程端口服务端
    import socket #导入模块
    import threading
    def recv_msg(socket,addr):
    	while True:
    		data = socket.recv(1024) #接受服务端发送的信息
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
    			socket.send(res_data.encode('UTF-8'))  # send byte data
    		except Exception as error:
    			print('send_send_send_', error)
    			socket.close()
    			break
    			
    
    
    server = socket.socket()#建立一个服务端
    host = '127.0.0.1'   #获取主机ip地址
    port = 9921#设置端口
    server.bind((host,port))#绑定端口
    server.listen(5) #等待连接
    c,addr = server.accept() #建立连接
    
    t_recv = threading.Thread(target=recv_msg,args=(c,addr))
    t_send = threading.Thread(target=send_msg,args=(c,addr))
    t_send.start()
    t_recv.start()
#先启动端口转发程序或者远程端口服务端，最后启动本地客户端
