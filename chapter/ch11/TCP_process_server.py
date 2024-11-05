'''
실습일: 2024.11.05
실습자: 201910852 심기윤
실습내용: TCP 에코 서버 실습
'''
#TCP 프로세싱 서버 프로그램
#숫자를 받아 영어를 송신한다

import socket

#숫자에 대한 영어 사전
table = {'1':'one', '2': 'two', '3': 'three', '4': 'four', '5':'five', '6': 'six', '7': 'seven', '8': 'eight',\
'9': 'nine', '10': 'ten'}

s = socket.socket()                                         #AF_INET, SOCK_STREAM
host = socket.gethostname()
ip_addr = socket.gethostbyname(host)

print(f'서버 IP: {ip_addr}')

address = ("", 2500)
s.bind(address)

s.listen(1)
print('...클라이언트 연결 대기중...')

c_socket, c_addr = s.accept()
print(f"연결된 클라이언트: [ IP주소: {c_addr[0]} | 포트번호: {c_addr[1]} ]")

while True:
    data = c_socket.recv(1024).decode()                     #요청 수신
    print(f'받은 데이터: {data}', end="\t")
    try:
        resp = table[data]                                  #데이터를 key로 사용하여 value를 가져온다
    except:
        print("[올바르지 않은 입력값. 클라이언트로 재전송 요청] ")
        c_socket.send('다시 시도해주세요'.encode('utf-8'))     #오류가 있을 때
    else:
        print(f"[올바른 입력값. {data}에 알맞은 값인 {resp} 전송] ")
        c_socket.send(resp.encode())                        #변환 값을 전송