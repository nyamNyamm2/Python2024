'''
실습일: 2024.11.19
실습자: 201910852 심기윤
실습내용: GUI 클라이언트 실습
'''

# 섭씨 온도를 보내고 화씨 온도를 받아 표시하는 GUI 클라이언트 프로그램

import tkinter as tk
from tkinter import *
from socket import *
import threading
from tkinter import messagebox


#섭씨 온도를 서버로 전송
def calculate():
    global temp
    try:
        temp = float(entry1.get())      # 사용자가 입력한 값을 float으로 변환
        sock.send(str(temp).encode())   # 서버로 전송
    except ValueError:                  # 입력값이 숫자가 아닌 경우
        messagebox.showerror("입력 오류", "숫자 값을 입력해주세요!")  # 팝업 알림창 표시
        entry1.delete(0, tk.END)    # 입력 필드를 초기화

#Thread handler
def handler(sock):
    while True:
        try:                            # 수신 데이터가 없으면 예외 발생
            r_msg = sock.recv(1024)     # 메시지 수신
        except:                         # 수신 데이터 없음
            pass
        else:                           # 수신 데이터 표시
            entry2.delete(0, END)
            entry2.insert(0, r_msg.decode())
            entry1.delete(0, END)

# 소켓 설정
sock = socket(AF_INET, SOCK_STREAM)
sock.connect(("localhost", 2500))

# GUI 설정
# entry1 = 섭씨온도(사용자가 입력)
root = Tk()
message_label = Label(text='Enter a temperature(C)  ',font=('Verdana', 16))
entry1 = Entry(font=('Verdana', 16), width=5)

# entry2 = 화씨온도(서버에서 계산한 결과)
recv_label = Label(text='Temperature in F  ',font=('Verdana', 16))
entry2 = Entry(font=('Verdana', 16), width=5)

# 버튼 클릭 시 calculate 함수 실행
calc_button = Button(text='전송', font=('Verdana', 12), command=calculate)

# 각 위치 설정(grid 정렬)
message_label.grid(row=0, column=0, sticky=W)
recv_label.grid(row=1, column=0, sticky=W)
entry1.grid(row=0, column=1)
entry2.grid(row=1, column=1)
calc_button.grid(row=0, column=2, padx=10, pady=10)

#데이터 수신을 위한 스레드 생성과 실행
cThread = threading.Thread(target=handler, args=(sock,))
cThread.daemon = True
cThread.start()

mainloop()
