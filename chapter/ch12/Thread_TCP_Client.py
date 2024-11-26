'''
실습일: 2024.11.19
실습자: 201910852 심기윤
실습내용: Threading 클라이언트 실습
'''

#threading.Thread를 이용한 TCP client program
#Thread_TCP_client.py

import socket
import threading

# 함수로 작성하여 실행 시 스레드
def handler(sock):
    
    while True:
        data = sock.recv(1024)
        print('\n받은 메시지: ',data.decode())
        
# 소켓 생성
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

while True:
    print("연결 종료 원할 시 입력창에 'q'입력")

    # ip 매핑
    host = input("서버 IP주소(default=127.0.0.1): ").strip()
    if host == '':
        host = '127.0.0.1'
    elif host == 'q':
        break


    print("연결 종료 원할 시 입력창에 '9999'입력")

    # 포트 번호 입력
    port = input("포트 번호(default: 2500): ").strip()
    if port == '':
        port = 2500
    elif port == '9999':
        break
    else:
        port = int(port)
    

    # 서버 연결
    sock.connect((host, port))
    print(f"연결된 서버 >> {host}:{port}")

    # 스레드 설정
    cThread = threading.Thread(target=handler, args=(sock,))
    cThread.daemon = True
    cThread.start()

    
    # 실행 코드
    print("연결 종료 원할 시 입력창에 'q'입력")
    while True:
        msg = input(' ')
        if msg == 'q':
            print("서버와 연결을 종료합니다.\n")
            break
        sock.send(msg.encode())

sock.close()
print("\n\n* * * * * * 연결 종료 * * * * * *\n\n")