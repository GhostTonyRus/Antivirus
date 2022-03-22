import socket

ip = "127.0.0.1"
port = 12345

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((ip, port))
client.sendall("create table".encode("utf-8"))
# data = client.recv(2048)
# print(data)
client.close()
