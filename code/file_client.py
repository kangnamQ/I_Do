#파일 전송 클라이언트 프로그램
from socket import *
import os
import sys
import time

now = time.localtime()
now_time = (f"{now.tm_year}/{now.tm_mon}/{now.tm_mday} {now.tm_hour}:{now.tm_min}:{now.tm_sec}")

print("="*59)
print("클라이언트 네트워크 초기화 중입니다. 잠시 기다려 주십시오.")
print("="*59)

serverName = '127.0.0.1'
serverPort = 2020
clientSocket = socket(AF_INET, SOCK_STREAM)

clientSocket.connect((serverName, serverPort))

print("-"*23)
print("서버가 연결되었습니다.")
print("-"*23)

filename = input('전송할 파일을 입력하여 주세요 : ')
clientSocket.send(filename.encode('utf-8'))

data = clientSocket.recv(1024)
data_trans = 0

if not data:
    print(f"파일 {filename}이 존재하지 않습니다.")
    sys.exit()

dir_now = os.getcwd()
with open(dir_now + "\\" + filename, 'wb') as f:
    try:
        while data:
            f.write(data)
            data_trans += len(data)
            data = clientSocket.recv(1024)
    except Exception as error:\
            print(error)
print(f"파일 {filename} 받기 완료. | 전송량 : {data_trans}")
print(f"파일 전송 시간 : [" + now_time + "]")

