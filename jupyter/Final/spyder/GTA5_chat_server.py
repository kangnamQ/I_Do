# -*- coding: utf-8 -*-
"""
GTA 5 채팅 서버 프로그램
"""


from socket import *
from threading import *
import time

exec(open("GTA5.py").read())

now = time.localtime()
now_time = (f"{now.tm_year}/{now.tm_mon}/{now.tm_mday} {now.tm_hour}:{now.tm_min}:{now.tm_sec}")

def serverRecv():
    while True:
        clientMsg = connectionSocket.recv(1024)
        print(f"["+now_time+"] " + " [클라이언트] : " + clientMsg.decode("utf8") + "\n")


print("="*52)
print("서버 네트워크 초기화 중입니다. 잠시 기다려 주십시오.")
print("="*52)

try:
    Port = int(input("서버의 포트를 입력하여 주십시오."))
except ValueError:
    print("기본값 2020으로 설정되었습니다.")
    Port = 2020

serverPort = Port
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)

connectionSocket, addr = serverSocket.accept()

print("-"*53)
print(addr, "에서 클라이언트가 연결되었습니다.")
print("-"*53)

Thread(target = serverRecv).start()


while True:
    now = time.localtime()
    now_time = (f"{now.tm_year}/{now.tm_mon}/{now.tm_mday} {now.tm_hour}:{now.tm_min}:{now.tm_sec}")

    msg = input("["+now_time+"] "+" 나 : ")
    print("")
    connectionSocket.send(msg.encode("utf8"))


connectionSocket.close()

