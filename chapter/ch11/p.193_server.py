'''
실습일: 2024.11.05
실습자: 201910852 심기윤
실습내용: TCP 소켓 실습
'''

import socket
import time

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
address = ('', 5000)
sock.bind(address)
sock.listen(5)

cnt = 0

while True:
    client, addr = sock.accept()
    print("Connection requested from", addr)

    cnt += 1
    if cnt == 1:
        print(f"프로그램 처음 접속자: {addr}\n")
        client.send(f'당신은 {cnt}번째 접속자 입니다 '.encode('utf-8'))

    client.send(time.ctime(time.time()).encode())

    client.close()

