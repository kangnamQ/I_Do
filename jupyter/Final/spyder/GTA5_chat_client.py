# -*- coding: utf-8 -*-
"""
GTA 5 채팅 클라이언트 프로그램
"""


from socket import *
from threading import *
import time

now = time.localtime()
now_time = (f"{now.tm_year}/{now.tm_mon}/{now.tm_mday} {now.tm_hour}:{now.tm_min}:{now.tm_sec}")

def clientRecv():
    while True:
        serverMsg = clientSocket.recv(1024)
        print(f"["+now_time+"] " + " [서버] : " + serverMsg.decode("utf8") + "\n")

    clientSocket.close()

print("="*59)
print("클라이언트 네트워크 초기화 중입니다. 잠시 기다려 주십시오.")
print("="*59)

serverName = '127.0.0.1'
try:
    Port = int(input("서버의 포트를 입력하여 주십시오."))
except ValueError:
    print("기본값 2020으로 설정되었습니다.")
    Port = 2020
    
serverPort = Port
clientSocket = socket(AF_INET, SOCK_STREAM)

clientSocket.connect((serverName, serverPort))

print("-"*64)
print("서버가 연결되었습니다. 채팅을 두 번 치신 후에 대화가 시작됩니다." )
print("-"*64)

Thread(target = clientRecv).start()

while True:
    now = time.localtime()
    now_time = (f"{now.tm_year}/{now.tm_mon}/{now.tm_mday} {now.tm_hour}:{now.tm_min}:{now.tm_sec}")

    msg = input("[" + now_time + "] " + " 나 : ")
    print("")
    clientSocket.send(msg.encode("utf8"))



clientSocket.close()
