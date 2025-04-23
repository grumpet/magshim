#q1
import socket
DOMAIN = 'networks.cyber.org.il'
PORT = 8820

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = (DOMAIN, PORT)
sock.connect(server_address)
print(f'Connected to {DOMAIN} on port {PORT}')

sock.sendall(b'mip')

server_message = sock.recv(1024).decode()
print(f'Server: {server_message}')

