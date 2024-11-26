'''
실습일: 2024.11.26
실습자: 201910852 심기윤
실습내용: GUI 체팅 서버 UDP 실습
'''

# UDP 채팅 서버 프로그램

import socket
import time

host = ''
port = 2500
BUFFER_SIZE = 1024

clients = [] #클라이언트 리스트

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host, port))
s.setblocking(0)

print('서버 시작됨')

while True:
    try:
        data, addr = s.recvfrom(BUFFER_SIZE) #수신 데이터가 없으면 반복 시도
        if "quit" in data.decode():
            if addr in clients:
                clients.remove(addr)
                print(f'클라이언트 {addr}가 떠났습니다')
        elif addr not in clients: #클라이언트 리스트에 없으면 추가
            print(f"새로운 클라이언트 ID: {data.decode()}{addr}")
            clients.append(addr)
            continue
        print(time.ctime(time.time()) + str(addr) + ': :' + data.decode())
        for client in clients: #모든 클라이언트에게 전송
            if client != addr and data:
                s.sendto(data, client)
    except:
        pass
s.close()