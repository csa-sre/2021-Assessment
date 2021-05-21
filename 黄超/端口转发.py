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
#本机ip地址和端口
local_host = '192.168.79.128'
local_port = 9922
#远端ip地址和端口
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
