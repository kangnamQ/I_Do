#채팅 클라이언트 프로그램
from socket import *
from threading import *

def clientRecv():
    while True:
        serverMsg = clientSocket.recv(1024)
        print("[서버]" + serverMsg.decode("utf8") + "\n")

    clientSocket.close()


print("클라이언트 네트워크 연결 초기화 .....")

serverName = '127.0.0.1'
serverPort = 9000
clientSocket = socket(AF_INET, SOCK_STREAM)


clientSocket.connect((serverName, serverPort))
print("서버 연결됨...\n")

Thread(target = clientRecv).start()

while True:
    msg = input()
    clientSocket.send(msg.encode("utf8"))

clientSocket.close()
