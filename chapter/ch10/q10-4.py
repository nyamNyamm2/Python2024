'''
실습일: 2024.10.29
실습자: 201910852 심기윤
실습내용: 문자열인 도메인 주소의 ip주소를 찾고 ip주소의 문자열 주소를 찾기
'''
import socket

host = input("도메인 주소 입력: ")
ip = input("ip 주소 입력: ")


try:
    print(host)
    hostname, aliases, addresses = socket.gethostbyname_ex(host)
    print(f'Hostname: {hostname}')
    print(f'Aliases: {aliases}')
    print(f'Addresses: {addresses}')
except socket.error as msg:
    print(f'Socket error: {msg}')
print()


try:
    print(ip)
    hostname, aliases, addresses = socket.gethostbyaddr(ip)
    print('Hostname :', hostname)
    print('Aliases  :', aliases)
    print('Addresses:', addresses)
except socket.error as msg:
    print(f'Socket error: {msg}')
print()