#채팅 서버 프로그램
from socket import *
from threading import *
from select import *
import time

def serverRecv():
    while True:
        clientMsg = client_Socket.recv(size)
        print("[클라이언트]" + clientMsg.decode("utf8") + "\n")

now = time.localtime()
now_time = (f"{now.tm_year}/{now.tm_mon}/{now.tm_mday} {now.tm_hour}:{now.tm_min}:{now.tm_sec}")

print("="*52)
print("서버 네트워크 초기화 중입니다. 잠시 기다려 주십시오.")
print("="*52)

#추가하기 편하도록 따로따로 정의
ip = ''
serverPort1 = 2020
serverPort2 = 2030
serverPort3 = 2040
size = 1024
addr1 = (ip, serverPort1)
addr2 = (ip, serverPort2)
addr3 = (ip, serverPort3)

serverSocket1 = socket(AF_INET, SOCK_STREAM)
serverSocket1.bind(addr1)
serverSocket1.listen(1)

serverSocket2 = socket(AF_INET, SOCK_STREAM)
serverSocket2.bind(addr2)
serverSocket2.listen(1)

serverSocket3 = socket(AF_INET, SOCK_STREAM)
serverSocket3.bind(addr3)
serverSocket3.listen(1)

read_socket_list = [serverSocket1, serverSocket2, serverSocket3]

while True:
    now = time.localtime()
    now_time = (f"{now.tm_year}/{now.tm_mon}/{now.tm_mday} {now.tm_hour}:{now.tm_min}:{now.tm_sec}")

    #select.select(rlist, wlist, xlist[, timeout])
    rlist, wlist, xlist = select(read_socket_list, [], [])
    for i in rlist:
        if i == serverSocket1:
            print("1번 참가자님 환영합니다. 어서오세요.")
            client_Socket, client_addr = serverSocket1.accept()
            print("-" * 53)
            print(client_addr, "에서 클라이언트가 연결되었습니다.")
            print("-" * 53)
            clientMsg = client_Socket.recv(size)
            print(f"[" + now_time + "] ", client_addr, " : " + clientMsg.decode("utf8") + "\n")

            msg = input()
            client_Socket.send(msg.encode("utf8"))



        elif i == serverSocket2:
            print("2번 참가자님 환영합니다. 어서오세요.")
            client_Socket, client_addr = serverSocket2.accept()
            print("-" * 53)
            print(client_addr, "에서 클라이언트가 연결되었습니다.")
            print("-" * 53)
            clientMsg = client_Socket.recv(size)
            print(f"[" + now_time + "] ", client_addr, " : " + clientMsg.decode("utf8") + "\n")

            msg = input()
            client_Socket.send(msg.encode("utf8"))


        elif i == serverSocket3:
            print("3번 참가자님 환영합니다. 어서오세요.")
            client_Socket, client_addr = serverSocket3.accept()
            print("-" * 53)
            print(client_addr, "에서 클라이언트가 연결되었습니다.")
            print("-" * 53)
            clientMsg = client_Socket.recv(size)
            print(f"[" + now_time + "] ", client_addr, " : " + clientMsg.decode("utf8") + "\n")

            msg = input()
            client_Socket.send(msg.encode("utf8"))

client_Socket.close()

