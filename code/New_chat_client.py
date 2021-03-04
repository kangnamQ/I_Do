#채팅 클라이언트 프로그램
from socket import *
from threading import *
import time

now = time.localtime()
now_time = (f"{now.tm_year}/{now.tm_mon}/{now.tm_mday} {now.tm_hour}:{now.tm_min}:{now.tm_sec}")

def clientRecv():
    while True:
        serverMsg = clientSocket.recv(size)
        print(f"["+now_time+"] " + " [서버] : " + serverMsg.decode("utf8") + "\n")

    clientSocket.close()

print("="*59)
print("클라이언트 네트워크 초기화 중입니다. 잠시 기다려 주십시오.")
print("="*59)

serverName = '127.0.0.1'
serverPort = 2020
size = 1024
clientSocket = socket(AF_INET, SOCK_STREAM)

clientSocket.connect((serverName, serverPort))

print("-"*23)
print("서버가 연결되었습니다.")
print("-"*23)

Thread(target = clientRecv).start()

while True:
    now = time.localtime()
    now_time = (f"{now.tm_year}/{now.tm_mon}/{now.tm_mday} {now.tm_hour}:{now.tm_min}:{now.tm_sec}")

    msg = input("[" + now_time + "] " + " 나 : ")
    print("")
    clientSocket.send(msg.encode("utf8"))


clientSocket.close()
