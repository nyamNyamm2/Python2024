'''
실습일: 2024.10.29
실습자: 201910852 심기윤
실습내용: socket 실습
'''

# IP 주소를 이용한 호스트 이름 찾기 프로그램

import socket

hostname, aliases, addresses = socket.gethostbyaddr('66.33.211.242')

print('Hostname :', hostname)
print('Aliases  :', aliases)
print('Addresses:', addresses)