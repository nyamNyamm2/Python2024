'''
실습일: 2024.10.29
실습자: 201910852 심기윤
실습내용: gethostbyname 함수의 사용법과 'SOCK_STREAM', 'SOCK_DGRAM'의 속성값 확인
'''

# 파이썬 콘솔로 실행

import socket

getattr(socket, 'SOCK_STREAM')
getattr(socket, 'SOCK_DGRAM')