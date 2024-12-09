import socket
import threading
import tkinter as tk
from tkinter import scrolledtext
from tkinter import messagebox

def receive_messages():
    while True:
        try:
            message = client_socket.recv(1024).decode()
            if message.startswith("접속자 목록:"):
                users = message.replace("접속자 목록:", "").strip()
                user_list.config(state=tk.NORMAL)
                user_list.delete(1.0, tk.END)
                user_list.insert(tk.END, users + '\n')
                user_list.config(state=tk.DISABLED)
            else:
                chat_area.config(state=tk.NORMAL)
                chat_area.insert(tk.END, message + '\n', 'chat')
                chat_area.config(state=tk.DISABLED)
                chat_area.see(tk.END)
        except:
            print("오류가 발생했습니다. 종료합니다...")
            client_socket.close()
            break

def send_message(event=None):
    message = input_area.get()
    input_area.delete(0, tk.END)
    client_socket.send(message.encode())
    chat_area.config(state=tk.NORMAL)
    chat_area.insert(tk.END, f"나: {message}\n", 'chat')
    chat_area.config(state=tk.DISABLED)
    chat_area.see(tk.END)
    if message == "EXIT":
        client_socket.close()
        app.quit()

def start_game():
    client_socket.send("START_GAME".encode())

def send_guess():
    guess = guess_input.get()
    guess_input.delete(0, tk.END)
    client_socket.send(f"GUESS:{guess}".encode())

def connect_to_server():
    global client_socket
    host = host_input.get()
    port = port_input.get()
    username = username_input.get()

    if not host or not port or not username:
        messagebox.showerror("입력 오류", "모든 필드를 채워주세요.")
        return

    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((host, int(port)))
        client_socket.send(f"USERNAME:{username}".encode())
        connection_window.destroy()
    except Exception as e:
        messagebox.showerror("연결 오류", f"서버에 연결할 수 없습니다: {e}")

# Initial connection setup window
connection_window = tk.Tk()
connection_window.title("서버 연결 설정")

connection_frame = tk.Frame(connection_window)

host_label = tk.Label(connection_frame, text="서버 IP:")
host_label.grid(row=0, column=0, padx=5, pady=5)
host_input = tk.Entry(connection_frame, width=30)
host_input.insert(0, "127.0.0.1")
host_input.grid(row=0, column=1, padx=5, pady=5)

port_label = tk.Label(connection_frame, text="서버 포트:")
port_label.grid(row=1, column=0, padx=5, pady=5)
port_input = tk.Entry(connection_frame, width=30)
port_input.insert(0, "12345")
port_input.grid(row=1, column=1, padx=5, pady=5)

username_label = tk.Label(connection_frame, text="사용자 이름:")
username_label.grid(row=2, column=0, padx=5, pady=5)
username_input = tk.Entry(connection_frame, width=30)
username_input.grid(row=2, column=1, padx=5, pady=5)

connect_button = tk.Button(connection_frame, text="연결", command=connect_to_server)
connect_button.grid(row=3, column=0, columnspan=2, pady=10)

connection_frame.pack(padx=10, pady=10)
connection_window.mainloop()

# Main chat and game window
app = tk.Tk()
app.title("숫자 야구 게임")

# Layout setup
main_frame = tk.Frame(app)
main_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Chat area
chat_frame = tk.Frame(main_frame)
chat_area = scrolledtext.ScrolledText(chat_frame, wrap=tk.WORD, state=tk.DISABLED, height=20, width=50)
chat_area.tag_config('chat', foreground='blue')
chat_area.pack(padx=10, pady=(10, 0))

input_area = tk.Entry(chat_frame, width=50)
input_area.pack(padx=10, pady=(0, 10))
input_area.bind("<Return>", send_message)
chat_frame.pack(side=tk.LEFT, fill=tk.Y)

# User list area
game_frame = tk.Frame(main_frame)

status_label = tk.Label(game_frame, text="접속한 사용자:", font=("Arial", 12, "bold"))
status_label.pack(pady=(10, 5))

user_list = scrolledtext.ScrolledText(game_frame, wrap=tk.WORD, state=tk.DISABLED, height=10, width=40)
user_list.pack(padx=10, pady=(0, 10))

# Guessing game area
guess_label = tk.Label(game_frame, text="숫자를 입력하세요:")
guess_label.pack()

guess_input = tk.Entry(game_frame, width=30)
guess_input.pack(pady=5)

submit_guess_button = tk.Button(game_frame, text="추측 제출", command=send_guess)
submit_guess_button.pack(pady=5)

start_button = tk.Button(game_frame, text="게임 시작", command=start_game)
start_button.pack(pady=5)

game_frame.pack(side=tk.RIGHT, fill=tk.Y)

# Start receiving thread
receive_thread = threading.Thread(target=receive_messages)
receive_thread.daemon = True
receive_thread.start()

app.mainloop()
