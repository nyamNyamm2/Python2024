'''
실습일: 2024.11.05
실습자: 201910852 심기윤
실습내용: TCP 소켓 실습
'''

import socket
from datetime import datetime

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 5000))

data = sock.recv(1024).decode()

dt = datetime.strptime(data, "%a %b %d %H:%M:%S %Y")

format_date = dt.strftime("%Y %b %d (%a) %H:%M:%S")

print(f"현재 시각: {format_date}")
sock.close()