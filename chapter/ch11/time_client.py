'''
실습일: 2024.11.05
실습자: 201910852 심기윤
실습내용: TCP 소켓 실습
'''

import socket

# socket() 소켓 생성
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect() 연결 요청
sock.connect(('localhost', 5000))

print("현재 시각: ", sock.recv(1024).decode())
sock.close()