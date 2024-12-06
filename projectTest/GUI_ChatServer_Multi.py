# threading 모듈을 이용한 TCP 멀티 채팅 서버 프로그램

from socket import *
from threading import *

PORT_NUM = 2500
BUFFER_SIZE = 1024

class MultiChatServer:

    def __init__(self, port):
        self.clients = []  # 접속된 클라이언트 소켓 목록
        self.s_sock = socket(AF_INET, SOCK_STREAM)
        self.ip = ''
        self.port = port
        self.s_sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        self.s_sock.bind((self.ip, self.port))
        print("\n* * * * * 서버 활성화 * * * * *\n\n* * * 클라이언트 연결 허용 * * *\n\n")
        self.s_sock.listen(100)
        self.accept_client()

    def accept_client(self):
        while True:
            client = c_socket, (ip, port) = self.s_sock.accept()
            if client not in self.clients:
                self.clients.append(client)
            print(f'({ip}, {str(port)})가 연결되었습니다.')
            cth = Thread(target=self.receive_messages, args=(c_socket,))
            cth.start()

    def receive_messages(self, c_socket):
        while True:
            try:
                incoming_message = c_socket.recv(BUFFER_SIZE)
                if not incoming_message:
                    break
            except:
                continue
            else:
                message = incoming_message.decode('utf-8')
                if message.startswith("CTOF:"):
                    self.handle_ctof_request(c_socket, message)
                else:
                    self.send_all_clients(c_socket, message)
        c_socket.close()

    def handle_ctof_request(self, c_socket, message):
        '''
        섭씨 -> 화씨 변환 후 클라이언트에게 전송
        '''
        try:
            fahrenheit = float(message[5:])
            response = f"화씨 온도는 {fahrenheit:.2f}°F입니다."
            c_socket.send(response.encode('utf-8'))
        except ValueError:
            c_socket.send("잘못된 값입니다.".encode('utf-8'))

    def send_all_clients(self, senders_socket, message):
        for client in self.clients:
            socket, (ip, port) = client
            if socket is not senders_socket:
                try:
                    socket.sendall(message.encode('utf-8'))
                except:
                    self.clients.remove(client)
                    print(f"({ip}, {port}) 연결이 종료되었습니다")


if __name__ == "__main__":
    MultiChatServer(PORT_NUM)
