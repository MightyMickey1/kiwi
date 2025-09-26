import socket

clientMsg = 'Good morning, Shiron'.encode('utf-8')
serverAddr = ('192.168.000', 5268)
bufferSize = 1024

UDPClient = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
UDPClient.sendto(clientMsg, serverAddr)
serverMsg, addr = UDPClient.recvfrom(bufferSize)
serverMsg = serverMsg.decode('utf-8')

print('Data from server: ', serverMsg)
print(f'Server Addess: {addr[0]}:{addr[1]}')