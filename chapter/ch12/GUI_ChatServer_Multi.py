'''
실습일: 2024.11.19
실습자: 201910852 심기윤
실습내용: GUI 체팅 서버 실습
'''

# threading 모듈을 이용한 TCP 멀티 채팅 서버 프로그램

from socket import *
from threading import *

PORT_NUM = 2500
BUFFER_SIZE = 1024

class MultiChatServer:

    #소켓을 생성하고 연결되면 accept_client() 호출
    def __init__(self, port):
        self.clients = []                                                   # 접속된 클라이언트 소켓 목록
        self.final_received_message = ""                                    # 최종 수신 메시지
        self.s_sock = socket(AF_INET, SOCK_STREAM)
        self.ip = ''
        self.port = port
        self.s_sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        self.s_sock.bind((self.ip, self.port))
        print("* * * * * 서버 활성화 * * * * *\n* * * 클라이언트 연결 허용 * * *\n\n")
        self.s_sock.listen(100)
        self.accept_client()
        
    #클라이언트 소켓을 목록에 추가하고 스레드를 생성하여 데이터를 수신한다
    def accept_client(self):
        while True:
            client = c_socket, (ip, port) = self.s_sock.accept()
            if client not in self.clients:
                self.clients.append(client)                                 # 접속된 소켓을 목록에 추가
            print (f'({ip}, {str(port)})가 연결되었습니다.')
            cth = Thread(target=self.receive_messages, args=(c_socket,))    # 수신 스레드
            cth.start() #스레드 시작

            
    #데이터를 수신하여 모든 클라이언트에게 전송한다
    def receive_messages(self, c_socket):
        while True:
            try:
                incoming_message = c_socket.recv(BUFFER_SIZE)
                if not incoming_message:                                    # 연결이 종료됨
                    break
            except:
                continue
            else:
                self.final_received_message = incoming_message.decode('utf-8')
                print(self.final_received_message)
                self.send_all_clients(c_socket)
        c_socket.close()
        
    #송신 클라이언트를 제외한 모든 클라이언트에게 메시지 전송
    def send_all_clients(self, senders_socket):
        for client in self.clients:
            socket, (ip, port) = client
            if socket is not senders_socket:                                # 송신 클라이언트는 제외
                try:
                    socket.sendall(self.final_received_message.encode('utf-8'))
                except:                                                     # 연결 종료
                   self.clients.remove(client)                              # 소켓 제거
                   print(f"({ip}, {port}) 연결이 종료되었습니다")
        
            
if __name__ == "__main__":
    MultiChatServer(PORT_NUM)
