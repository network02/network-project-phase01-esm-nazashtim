import socket

client = socket.socket(socket.AF_INET , socket.SOCK_STREAM)                                

server = 'localhost'
port = 8080
addr=(server,port)

client.connect(addr)

#request = f"POST Taha 20 HTTP/1.1\r\nHost: {server}:{port}\r\n\r\n"  
request = f"GET user4 HTTP/1.1\r\nHost: {server}:{port}\r\n\r\n"  

client.send(request.encode("utf-8"))

response= client.recv(4096)

print(response.decode("utf-8"))
