import socket

HOST = '192.168.0.13' # local 호스트 사용
PORT = 10000 # 10000번 포트 사용
# 소켓 생성
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 접속
client_socket.connect((HOST, PORT))

while True:
    sendData = input("input data :")
    client_socket.send(sendData.encode('utf-8'))
client_socket.close()