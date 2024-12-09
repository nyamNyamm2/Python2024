import socket
import threading
import random

clients = []
usernames = {}
game_state = {
    "active": False,
    "turn": None,
    "answer": "",
    "guesses": []
}

def generate_random_answer():
    return "".join(random.sample("123456789", 3))

def calculate_strike_and_ball(answer, guess):
    strikes = sum(1 for a, g in zip(answer, guess) if a == g)
    balls = sum(1 for g in guess if g in answer) - strikes
    return strikes, balls

def handle_client(client_socket, address):
    global game_state
    while True:
        try:
            message = client_socket.recv(1024).decode()
            if not message:
                break

            if message.startswith("USERNAME:"):
                username = message.split(":")[1]
                usernames[address] = username
                clients.append((client_socket, address))
                broadcast(f"{username}님이 게임에 접속했습니다!\n")
                send_client_list()  # 접속자 목록 전송

            elif message.startswith("START_GAME"):
                if not game_state["active"]:
                    game_state["active"] = True
                    game_state["answer"] = generate_random_answer()
                    game_state["turn"] = list(usernames.keys())[0]
                    broadcast("게임이 시작되었습니다! 첫 번째 턴: " + usernames[game_state["turn"]] + "\n")

            elif message.startswith("GUESS:"):
                guess = message.split(":")[1]
                if len(guess) != 3 or not guess.isdigit():
                    client_socket.send("숫자 3개를 입력해야 합니다!\n".encode())
                    continue

                if game_state["active"] and address == game_state["turn"]:
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
    del usernames[address]
    broadcast(f"{usernames.get(address, address)}님이 연결을 종료했습니다.\n")
    send_client_list()  # 접속자 목록 갱신

def broadcast(message, sender_socket=None):
    for client, _ in clients:
        if client != sender_socket:
            try:
                client.send(message.encode())
            except:
                pass

def send_client_list():
    client_list = [usernames[addr] for _, addr in clients]
    user_list_message = "접속자 목록:" + ", ".join(client_list)
    broadcast(user_list_message)

def reset_game():
    global game_state
    game_state = {
        "active": False,
        "turn": None,
        "answer": "",
        "guesses": []
    }

def next_turn():
    current_index = list(usernames.keys()).index(game_state["turn"])
    next_index = (current_index + 1) % len(usernames)
    game_state["turn"] = list(usernames.keys())[next_index]
    broadcast(f"다음 턴: {usernames[game_state['turn']]}\n")

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("0.0.0.0", 12345))
    server.listen(5)
    print("서버가 시작되었습니다. 연결을 기다리는 중...")

    while True:
        client_socket, client_address = server.accept()
        thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
        thread.start()

if __name__ == "__main__":
    main()
