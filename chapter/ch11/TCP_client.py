'''
실습일: 2024.11.05
실습자: 201910852 심기윤
실습내용: TCP 에코 클라이언트 실습
'''
# 에외처리를 한 TCP 클라이언트 프로그램
# 실행할 때 서버 주소와 포트를 지정한다.
# 지정하지 않으면 '127.0.0.1'과 2500 사용

import socket

# 소켓 설정
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

#서버 주소 입력
svrIP = input(("서버 IP(default: 127.0.0.1): "))
if svrIP == '':
    svrIP = '127.0.0.1'                             #기본 주소
    
#포트 번호 입력
try:
    port = int(input("포트 번호(default: 2500): "))
except ValueError:
    port = 2500
# port = input("포트 번호(default: 2500): ")
# if port == '':
#     port = 2500                                   #기본 포트
# else:
#     port = int(port)

# 서버 연결
sock.connect((svrIP, port))
print(f'연결된 서버 IP: {svrIP}')

while True:
    msg = input("보낼 메시지 입력 (종료: q): ")
    if msg == 'q':
        print("연결이 정상적으로 종료되었습니다.")
        break
    
    #송신 데이터가 없으면 다시 진행
    if not msg:
        continue
    
    try:                                            #데이터 전송
        sock.send(msg.encode())                     #메시지 전송
        
    except:                                         #연결이 종료됨
        print("연결이 종료되었습니다")
        break

    try:                                            #데이터 읽기
        msg = sock.recv(1024)
        if not msg:                                 # 연결이 해제되었으면 빈 문자열 수신
            print("연결이 종료되었습니다")
            break
        print(f'받은 메시지: {msg.decode()}')

    except:                                         #연결이 강제 종료됨
        print("연결이 종료되었습니다")
        break

sock.close()