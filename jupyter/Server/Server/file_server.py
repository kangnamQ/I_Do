#파일 전송 서버 프로그램
from socket import *
from os.path import exists
import sys
import time

now = time.localtime()
now_time = (f"{now.tm_year}/{now.tm_mon}/{now.tm_mday} {now.tm_hour}:{now.tm_min}:{now.tm_sec}")

print("="*52)
print("서버 네트워크 초기화 중입니다. 잠시 기다려 주십시오.")
print("="*52)

serverPort = 2020
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)

connectionSocket, addr = serverSocket.accept()

print("-"*53)
print(addr, "에서 클라이언트가 연결되었습니다.")
print("-"*53)


filename = connectionSocket.recv(1024)
print('받는 데이터 : ', filename.decode('utf-8'))
data_trans = 0

if not exists(filename):
    print("파일이 없습니다. 다시 확인하여 주세요.")
    sys.exit()


print(f"파일 {filename} 전송 시작")
with open(filename, 'rb') as f:
    try:
        data = f.read(1024)
        while data: #data가 다 떨어질때 까지 실행
            data_trans += connectionSocket.send(data) #1024바이트씩 더해줌
            data = f.read(1024)
    except Exception as error:\
        print(error)
print(f"전송완료 : {filename} | 전송량 : [{data_trans} KB]")
print(f"파일 전송 시간 : [" + now_time + "]")
