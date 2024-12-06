# main.py
from tkinter import *
from tkinter import messagebox

from GUI_chatclient import ChatClient  # chat_client.py에서 ChatClient 클래스를 임포트


def initialize_connect_gui():
    '''
    IP와 포트, 사용자 이름을 입력받는 초기 GUI 창
    '''

    def connect_to_server():
        nonlocal ip, port, username
        ip = ip_entry.get().strip()  # IP 입력값
        port = port_entry.get().strip()  # 포트 입력값
        username = name_entry.get().strip()  # 사용자 이름 입력값

        # 유효성 검사
        if not username:  # 사용자 이름이 비어있으면
            messagebox.showerror("입력 오류", "사용자 이름을 입력해야 합니다.")
            return
        if not ip:  # IP 주소가 비어있으면
            messagebox.showerror("입력 오류", "IP 주소를 입력해야 합니다.")
            return
        if not port.isdigit():  # 포트 번호가 숫자인지 확인
            messagebox.showerror("입력 오류", "포트 번호는 숫자로 입력해야 합니다.")
            return
        port = int(port)  # 포트 번호를 정수로 변환

        connect_root.destroy()  # 창 닫기

    # GUI 창 생성
    connect_root = Tk()
    connect_root.title("서버 연결 설정")

    # 레이블과 입력 필드 배치
    Label(connect_root, text="서버 IP 주소").grid(row=0, column=0, padx=10, pady=10)
    Label(connect_root, text="포트 번호").grid(row=1, column=0, padx=10, pady=10)
    Label(connect_root, text="사용자 이름").grid(row=2, column=0, padx=10, pady=10)

    # 입력 필드
    ip_entry = Entry(connect_root, width=20)
    port_entry = Entry(connect_root, width=20)
    name_entry = Entry(connect_root, width=20)

    ip_entry.grid(row=0, column=1, padx=10, pady=10)
    port_entry.grid(row=1, column=1, padx=10, pady=10)
    name_entry.grid(row=2, column=1, padx=10, pady=10)

    # 기본값 설정
    ip_entry.insert(0, "127.0.0.1")
    port_entry.insert(0, "2500")
    name_entry.insert(0, "손님")

    # 연결 버튼
    Button(connect_root, text="연결", command=connect_to_server).grid(row=3, column=0, columnspan=2, pady=10)

    # 창을 실행하여 사용자 입력 받기
    ip, port, username = None, None, None  # 기본값 설정
    connect_root.mainloop()

    return ip, port, username  # 입력값을 반환



if __name__ == "__main__":
    ip, port, username = initialize_connect_gui()
    if ip and port and username:  # 모든 값이 정상적으로 입력되었을 경우
        print(f"서버 연결 정보: IP={ip}, PORT={port}, 사용자 이름={username}")
        ChatClient(ip, port, username)  # ChatClient 인스턴스를 생성하여 실행
        mainloop()
