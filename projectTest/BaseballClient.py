import socket
import threading
import tkinter as tk
from tkinter import scrolledtext
from tkinter import messagebox


# 서버에서 메시지를 수신하여 화면에 출력하는 함수
def receive_messages():
    while True:
        try:
            # 서버로부터 수신된 메시지 (문자열)
            message = client_socket.recv(1024).decode()

            # 체팅과 사용자 목록 구분
            if message.startswith("접속자 목록:"):
                users = message.replace("접속자 목록:", "").strip()
                user_list.config(state=tk.NORMAL)           # (ScrolledText) 위젯 수정 가능
                user_list.delete(1.0, tk.END)         # 1행 0열부터 끝까지
                user_list.insert(tk.END, users + '\n')      # 위젯 끝네 users 문자열 삽입
                user_list.config(state=tk.DISABLED)         # 위젯 수정 불가
            else:
                chat_area.config(state=tk.NORMAL)           # 위젯 수정 가능

                # 메시지 내용에 따라 다른 색상으로 출력
                if message.startswith("게임이 시작되었습니다") or message.startswith("다음 턴:") or "님이" in message or "게임 종료" in message:
                    chat_area.insert(tk.END, message + '\n', 'server')  # 서버 메시지 (검은색)
                elif ":" in message:
                    chat_area.insert(tk.END, message + '\n', 'colon')   # 상대 메시지 (초록색)
                else:
                    chat_area.insert(tk.END, message + '\n', 'chat')    # 나의 메시지 (파란색)
                chat_area.config(state=tk.DISABLED)         # 위젯 수정 불가
                chat_area.see(tk.END)                       # 스크롤 텍스트 마지막 위치로 자동 이동
        except:
            print("오류가 발생했습니다. 종료합니다...")
            client_socket.close()
            break


# 사용자가 입력한 메시지를 서버로 전송하는 함수
def send_message(event=None):
    message = input_area.get()                              # 사용자 입력 메시지 (문자열)
    input_area.delete(0, tk.END)                       # 입력창 초기화
    client_socket.send(message.encode())
    chat_area.config(state=tk.NORMAL)
    chat_area.insert(tk.END, f"나: {message}\n", 'chat')
    chat_area.config(state=tk.DISABLED)
    chat_area.see(tk.END)
    if message == "EXIT":
        client_socket.close()
        app.quit()

# 서버에 게임 시작 신호를 보내는 함수
def start_game():
    client_socket.send("START_GAME".encode())

# 사용자가 숫자 추측을 서버로 전송하는 함수
def send_guess():
    guess = guess_input.get()  # 사용자 입력 추측 (str)
    guess_input.delete(0, tk.END)
    client_socket.send(f"GUESS:{guess}".encode())

# 서버에 연결하는 함수
def connect_to_server():
    global client_socket
    host = host_input.get()  # 서버 IP (str)
    port = port_input.get()  # 서버 포트 (str -> int 변환 필요)
    username = username_input.get()  # 사용자 이름 (str)

    if not host or not port or not username:
        messagebox.showerror("입력 오류", "모든 필드를 채워주세요.")
        return

    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 클라이언트 소켓 생성
        client_socket.connect((host, int(port)))  # 서버에 연결
        client_socket.send(f"USERNAME:{username}".encode())  # 사용자 이름 전송
        connection_window.destroy()
    except Exception as e:
        messagebox.showerror("연결 오류", f"서버에 연결할 수 없습니다: {e}")



# 서버 연결 설정 창 초기화
connection_window = tk.Tk()
connection_window.title("서버 연결 설정")

connection_frame = tk.Frame(connection_window)

host_label = tk.Label(connection_frame, text="서버 IP:")
host_label.grid(row=0, column=0, padx=5, pady=5)
host_input = tk.Entry(connection_frame, width=30)
host_input.insert(0, "127.0.0.1")  # 기본값: 로컬호스트
host_input.grid(row=0, column=1, padx=5, pady=5)

port_label = tk.Label(connection_frame, text="서버 포트:")
port_label.grid(row=1, column=0, padx=5, pady=5)
port_input = tk.Entry(connection_frame, width=30)
port_input.insert(0, "12345")  # 기본값: 12345
port_input.grid(row=1, column=1, padx=5, pady=5)

username_label = tk.Label(connection_frame, text="사용자 이름:")
username_label.grid(row=2, column=0, padx=5, pady=5)
username_input = tk.Entry(connection_frame, width=30)
username_input.grid(row=2, column=1, padx=5, pady=5)

connect_button = tk.Button(connection_frame, text="연결", command=connect_to_server)
connect_button.grid(row=3, column=0, columnspan=2, pady=10)

connection_frame.pack(padx=10, pady=10)
connection_window.mainloop()

# 메인 채팅 및 게임 창 초기화
app = tk.Tk()
app.title("숫자 야구 게임")

# 레이아웃 설정
main_frame = tk.Frame(app)
main_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# 채팅 영역
chat_frame = tk.Frame(main_frame)
chat_area = scrolledtext.ScrolledText(chat_frame, wrap=tk.WORD, state=tk.DISABLED, height=20, width=50)
chat_area.tag_config('chat', foreground='blue')  # 일반 채팅 메시지 (파란색)
chat_area.tag_config('colon', foreground='green')  # 콜론 포함 메시지 (초록색)
chat_area.tag_config('server', foreground='black')  # 서버 메시지 (검은색)
chat_area.pack(padx=10, pady=(10, 0))

input_area = tk.Entry(chat_frame, width=50)
input_area.pack(padx=10, pady=(0, 10))
input_area.bind("<Return>", send_message)
chat_frame.pack(side=tk.LEFT, fill=tk.Y)

# 사용자 목록 영역
game_frame = tk.Frame(main_frame)

status_label = tk.Label(game_frame, text="접속한 사용자:", font=("Arial", 12, "bold"))
status_label.pack(pady=(10, 5))

user_list = scrolledtext.ScrolledText(game_frame, wrap=tk.WORD, state=tk.DISABLED, height=10, width=40)
user_list.pack(padx=10, pady=(0, 10))

# 숫자 추측 게임 영역
guess_label = tk.Label(game_frame, text="숫자를 입력하세요:")
guess_label.pack()

guess_input = tk.Entry(game_frame, width=30)
guess_input.pack(pady=5)

button_frame = tk.Frame(game_frame)
button_frame.pack(pady=5)

submit_guess_button = tk.Button(button_frame, text="추측 제출", command=send_guess)  # 숫자 추측 버튼
submit_guess_button.pack(side=tk.LEFT, padx=5)

start_button = tk.Button(button_frame, text="게임 시작", command=start_game)  # 게임 시작 버튼
start_button.pack(side=tk.LEFT, padx=5)

game_frame.pack(side=tk.RIGHT, fill=tk.Y)

# 메시지 수신 스레드 시작
receive_thread = threading.Thread(target=receive_messages)
receive_thread.daemon = True
receive_thread.start()

app.mainloop()
