'''
실습일: 2024.11.05
실습자: 201910852 심기윤
실습내용: TCP 에코 클라이언트 실습
'''
#create_connection()을 이용한 TCP 클라이언트 프로그램

import socket


# # 포트번호, 주소, 메시지 크기 설정
# port = 2500
# address = ('localhost', port)
# BUFSIZE = 1024
# 
# # socket() 소켓 설정
# sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 
# # connect() 서버 연결
# sock.connect(address)


# TCP 소켓 생성과 연결 (위 과정 생략)
sock =socket.create_connection(('localhost',2500 ))

# while문으로 무한반복하면 됨
# 메시지 전송
message ="클라이언트 메시지"
print('sending: {}'.format (message))
sock.sendall(message.encode())

data =sock.recv(1024)                                   #데이터 수신
print('received: {}'.format (data.decode()))
print('closing socket')
sock .close ()                                          #연결 종료
