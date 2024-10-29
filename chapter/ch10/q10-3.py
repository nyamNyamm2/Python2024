'''
실습일: 2024.10.29
실습자: 201910852 심기윤
실습내용: www.naver.com에 대한 정보
'''
import socket

host = 'www.naver.com'

try:
    print(host)
    hostname, aliases, addresses = socket.gethostbyname_ex(host)
    print(f'Hostname: {hostname}')
    print(f'Aliases: {aliases}')
    print(f'Addresses: {addresses}')
except socket.error as msg:
    print(f'Socket error: {msg}')
print()