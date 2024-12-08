# threading 모듈을 이용한 TCP 멀티 채팅 서버 프로그램

from socket import *
from threading import *

import random

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
        self.s_sock.listen(100)
        self.game_started = False
        self.current_turn = 0  # 현재 턴
        self.secret_numbers = {}  # 각 클라이언트의 비밀 번호
        self.guesses = {}  # 각 클라이언트의 추측
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
                elif "님이 야구게임" in message:  # 게임 성공 메시지 처리
                    self.send_all_clients(c_socket, message)  # 모든 클라이언트에게 게임 성공 메시지 전송
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
            c_socket.send(response.encode('utf-8'))  # 실행한 클라이언트에게만 전송
        except ValueError:
            c_socket.send("잘못된 값입니다.".encode('utf-8'))  # 실행한 클라이언트에게만 전송

    def start_game(self, c_socket):
        if self.game_started:
            c_socket.send("이미 게임이 시작되었습니다.".encode('utf-8'))
            return

        self.game_started = True
        # 각 클라이언트에게 비밀 번호를 생성하고 시작 메시지 전송
        for client in self.clients:
            socket, (ip, port) = client
            secret_number = random.sample(range(1, 10), 3)
            self.secret_numbers[socket] = secret_number
            socket.send("게임이 시작되었습니다! 첫 번째 클라이언트부터 시작하세요.".encode('utf-8'))

        self.send_game_status()

    def handle_guess(self, c_socket, message):
        if not self.game_started:
            c_socket.send("게임이 시작되지 않았습니다.".encode('utf-8'))
            return

        guess = message[10:].strip()
        if len(guess) != 3 or not guess.isdigit() or len(set(guess)) != 3:
            c_socket.send("잘못된 입력! 숫자는 3자리여야 하며 중복되지 않아야 합니다.".encode('utf-8'))
            return

        self.guesses[c_socket] = list(map(int, guess))
        result = self.check_guess(c_socket)
        c_socket.send(result.encode('utf-8'))

        if self.check_game_end():
            self.end_game()

        self.move_turn()

    def check_guess(self, c_socket):
        guess = self.guesses[c_socket]
        secret_number = self.secret_numbers[c_socket]
        strikes = sum(1 for i in range(3) if guess[i] == secret_number[i])
        balls = sum(1 for i in range(3) if guess[i] in secret_number and guess[i] != secret_number[i])

        if strikes == 3:
            return "축하합니다! 3개의 숫자를 맞추었습니다."
        else:
            return f"{strikes} 스트라이크, {balls} 볼"

    def move_turn(self):
        self.current_turn += 1
        if self.current_turn >= len(self.clients):
            self.current_turn = 0  # 게임이 끝나면 첫 번째 클라이언트로 돌아갑니다.

        self.send_game_status()

    def send_game_status(self):
        current_client_socket = self.clients[self.current_turn][0]
        current_client_socket.send("당신의 차례입니다.".encode('utf-8'))

    def check_game_end(self):
        # 모든 클라이언트가 비밀 번호를 맞췄는지 확인
        for client in self.clients:
            socket, (ip, port) = client
            if len(self.guesses.get(socket, [])) < 3:
                return False
        return True

    def end_game(self):
        self.game_started = False
        for client in self.clients:
            socket, (ip, port) = client
            socket.send("게임이 끝났습니다.".encode('utf-8'))
        self.reset_game()

    def reset_game(self):
        self.secret_numbers.clear()
        self.guesses.clear()
        self.current_turn = 0
        self.send_game_status()

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
