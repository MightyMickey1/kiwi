import socket

# Setup socket link
welcomeClientMsg = 'Good morning, Michael'.encode('utf-8')
serverAddr = ('10.40.117.241', 5678)
bufferSize = 1024
UDPClient = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Establish first contact
UDPClient.sendto(welcomeClientMsg, serverAddr)
serverMsg, addr = UDPClient.recvfrom(bufferSize)
serverMsg = serverMsg.decode('utf-8')
print('Welcome from server: ', serverMsg)
print(f'Server Addess: {addr[0]}:{addr[1]}\n')
