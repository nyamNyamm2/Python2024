import socket
import threading
import random

'''
 필요 자료구조들
'''
clients = []                # 접속한 소켓 객체 저장하는 리스트
usernames = {}              # 접속한 소켓 객체에 따른 사용자 이름을 저장하는 딕셔너리
game_state = {              # 게임 상태 정보를 저장하는 딕셔너리
    "active": False,
    "turn": None,
    "answer": "",
    "guesses": []
}


'''
정답 생성 로직
'''
def generate_random_answer():
    answer = "".join(random.sample("123456789", 3))     # 랜덤이 반환한 리스트 문자열로 결합
    print(f"정답: {answer}\n")
    return answer


'''
스트라이크와 볼 계산 로직
'''
def calculate_strike_and_ball(answer, guess):                       # 제너레이터 표현식 사용
    strikes = sum(1 for a, g in zip(answer, guess) if a == g)       # 정답과 추측의 같은 인덱스 가진 값끼리 튜플로 묶어 각 자리 숫자 일치하는 지 확인
    balls = sum(1 for g in guess if g in answer) - strikes          # 추측 문자열의 각 자리 숫자가 답에 포함되는 지 검사(스트라이크 개수는 빼기)
    return strikes, balls


'''
클라이언트 관리 로직
'''
def handle_client(client_socket, address):
    global game_state                                               # 게임 상황 전역변수로 설정
    while True:
        try:
            message = client_socket.recv(1024).decode()             # 클라이언트에서 받은 메시지 디코드
            if not message:
                break

            # 메시지 헤더로 구분
            # 유저 접속
            if message.startswith("USERNAME:"):                     
                username = message.split(":")[1]                    # 문자열
                usernames[address] = username                       # address값을 key로 딕셔너리에 value(username) 저장
                clients.append((client_socket, address))
                broadcast(f"{username}님이 게임에 접속했습니다!\n")

                send_client_list()

            # 게임 시작
            elif message.startswith("START_GAME"):
                if not game_state["active"]:
                    game_state["active"] = True                                 # 게임 상태 변환
                    game_state["answer"] = generate_random_answer()             # 정답 생성
                    game_state["turn"] = list(usernames.keys())[0]              # 턴 부여
                    broadcast("게임이 시작되었습니다! 첫 번째 턴: " + usernames[game_state["turn"]] + "\n")

            # 게임 진행
            elif message.startswith("GUESS:"):
                guess = message.split(":")[1]                                   # 문자열 (추측한 숫자 3자리)
                if len(guess) != 3 or not guess.isdigit():                      
                    client_socket.send("숫자 3개를 입력해야 합니다!\n".encode())
                    continue

                if game_state["active"] and address == game_state["turn"]:      # 게임 실행중이고 자신의 턴이 맞다면
                    strikes, balls = calculate_strike_and_ball(game_state["answer"], guess)
                    broadcast(f"{usernames[address]}님의 추측 {guess}: {strikes} 스트라이크, {balls} 볼\n")
                    if strikes == 3:
                        broadcast(f"{usernames[address]}님이 정답 {guess}을(를) 맞췄습니다! 게임 종료!\n")
                        reset_game()
                    else:
                        next_turn()
                else:
                    client_socket.send("아직 당신의 턴이 아닙니다!\n".encode())

            else:
                broadcast(f"{usernames[address]}: {message}", client_socket)

        except Exception as e:
            print(f"에러 발생: {e}")
            break

    client_socket.close()
    clients.remove((client_socket, address))
    broadcast(f"{usernames.get(address, address)}님이 연결을 종료했습니다.\n")
    del usernames[address]
    send_client_list()  # 접속자 목록 갱신


'''
다른 사용자에세 메시지 전송 로직
'''
def broadcast(message, sender_socket=None):
    for client, _ in clients:                       # _는 해당 변수 값이 존재하지만 받지않겠다는 뜻
        if client != sender_socket:
            try:
                client.send(message.encode())
            except:
                pass


'''
접속한 사용자 정보 제공 로직
'''
def send_client_list():
    # 현재 접속 중인 사용자 이름 목록 생성 (리스트 컴프리헨션 사용)
    client_list = [usernames[addr] for _, addr in clients]
    user_list_message = "접속자 목록:" + ", ".join(client_list)

    # 모든 클라이언트에게 전송
    for client, _ in clients:
        try:
            client.send(user_list_message.encode())
        except:
            pass


'''
게임 초기화 로직
'''
def reset_game():
    global game_state
    game_state = {
        "active": False,
        "turn": None,
        "answer": "",
        "guesses": []
    }


'''
다음 턴 넘기는 로직
'''
def next_turn():
    current_index = list(usernames.keys()).index(game_state["turn"])    # 현재 턴 순서 인덱스 저장
    next_index = (current_index + 1) % len(usernames)                   # (현재 인덱스 + 1) % 전체 리스트 길이
    game_state["turn"] = list(usernames.keys())[next_index]             # 다음 턴 인덱스 지정
    broadcast(f"다음 턴: {usernames[game_state['turn']]}\n")


'''

'''
def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)          # TCP 소켓
    server.bind(("", 12345))                                            # 모든 네트워크 인터페이스 | 포트번호: 12345
    server.listen(5)                                                    # 최대 5개 연결 요청 대기열에 저장가능
    print("* * * * * * * * * * * * * * *\n * * * * * * * * * * * * * * \n* * * * * 서버 활성화 * * * * *\n * * * * * * * * * * * * * * \n* * * * * * * * * * * * * * *\n\n")

    while True:
        client_socket, client_address = server.accept()                 # 클라이언트 수락
        thread = threading.Thread(target=handle_client, args=(client_socket, client_address))   # 실행될 함수 지정(target) 및 인자(args) 전달
        thread.start()

if __name__ == "__main__":
    main()
