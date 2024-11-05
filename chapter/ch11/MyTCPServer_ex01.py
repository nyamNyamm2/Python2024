'''
실습일: 2024.11.05
실습자: 201910852 심기윤
실습내용: TCP 소켓 서버 클래스 이용한 서버 구현 1
'''
#사용자 정의 모듈을 이용한 에코 서버 프로그램

import MyTCPServer as ms

server = ms.TCPServer(2500)
print("클라이언트 연결 대기중...")
while True:
    if not server.connected:
        csock, caddr = server.accept()
        print(f'클라이언트 연결: [IP주소: {caddr[0]} | 포트번호: {caddr[1]}]')
    else:
        msg = server.receive()
        # 연결이 되어 있지 않으면 None이 반환됨
        if msg:
            print('수신메시지: ', msg)
            server.send(msg)
        else:
            print("클라이언트 연결 종료")
            break

server.disconnect()