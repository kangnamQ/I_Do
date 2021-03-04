#채팅 서버 프로그램
from socket import *
from threading import *

def serverRecv():
    while True:
        clientMsg = connectionSocket.recv(1024)
        print("[클라이언트]" + clientMsg.decode("utf8") + "\n")

print("서버 네트워크 연결 초기화 .....")
serverPort = 9000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
connectionSocket, addr = serverSocket.accept()
print("클라이언트 연결됨...", addr, "\n")

Thread(target = serverRecv).start()

while True:
    msg = input()
    connectionSocket.send(msg.encode("utf8"))

connectionSocket.close()

