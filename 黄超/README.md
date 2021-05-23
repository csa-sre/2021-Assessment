#用python实现简单的端口转发

##简介

利用python的socket实现端口转发

##使用场景
A服务器在内网，B服务器在公网，A、B服务器无法直接连接，但是C服务器既可以访问A服务器也可以访问B服务器，但A想向B发送数据，那么可以这样：

1.在C服务器上运行forwarding程序，同时监听A服务器和B服务器的端口这样两个端口就可以互相传递数据了

2.在B服务器上运行remote_server程序，与C服务器连接

3.在A服务器上运行local_client程序，与C服务器连接

这样A，B服务器就间接联系在一起可以互相传递数据了

##代码简介
```python
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
```
tcp_mapping_worker这个函数实现从一个服务接收数据并发送给另一个服务器属于forwarding代码的的核心部分

 ```python
    threading.Thread(target=tcp_mapping_worker,args=(c,s2)).start() 
    threading.Thread(target=tcp_mapping_worker,args=(s2,c)).start()
```
创建两个线程来实现A，B服务端的交互

remote_server和local_client两个程序跟之前写的tcp多线程聊天器差不多
需要注意的是如果A服务器输入 quit 连接就会中断
```python
    def recv_msg(client):
    	while True:
    		data = client.recv(1024)	
    		data_str=str(data.decode('utf-8'))
    		print('收到数据:%s' % ( data_str))
    		if data_str=='quit':
    			print('对方主动断开连接,终止连接' )
    			client.close()
    			break 
    			
    		
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
```    		
       

