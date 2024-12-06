# chat_client.py
from socket import *
from tkinter import *
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText
from threading import *

BUFFER_SIZE = 1024


class ChatClient:
    client_socket = None

    def __init__(self, ip, port, username):
        self.username = username  # 사용자 이름을 전달받음
        self.initialize_socket(ip, port)
        self.initialize_gui()
        self.listen_thread()

    def initialize_socket(self, ip, port):
        '''
        TCP socket을 생성하고 server에게 연결
        '''
        self.client_socket = socket(AF_INET, SOCK_STREAM)
        remote_ip = ip
        remote_port = port
        try:
            self.client_socket.connect((remote_ip, remote_port))
            print(f"연결된 서버: ({remote_ip}, {remote_port})")
        except Exception as e:
            messagebox.showerror("연결 실패", f"서버 연결에 실패했습니다: {str(e)}")
            self.root.quit()

    def send_chat(self):
        '''
        message를 전송하는 callback 함수
        '''
        senders_name = self.username  # name_widget 대신 전달받은 사용자 이름을 사용

        # 사용자 이름 유효성 검사
        if not senders_name:
            messagebox.showwarning("이름 미입력", "사용자 이름을 설정하세요.")
            return 'break'

        senders_name += ':'

        data = self.enter_text_widget.get(1.0, 'end').strip()
        message = (senders_name + data).encode('utf-8')
        self.chat_transcript_area.insert('end', message.decode('utf-8') + '\n')
        self.chat_transcript_area.yview(END)
        self.client_socket.send(message)
        self.enter_text_widget.delete(1.0, 'end')
        return 'break'

    def initialize_gui(self):
        '''
        위젯을 배치하고 초기화한다
        '''
        self.root = Tk()
        self.root.title("채팅 프로그램")

        fr = []
        for i in range(0, 5):
            fr.append(Frame(self.root))
            fr[i].pack(fill=BOTH)

        # 사용자 이름 레이블
        self.name_label = Label(fr[0], text=f"사용자 이름: {self.username}", fg="blue")
        self.recv_label = Label(fr[1], text="수신 메시지:")
        self.send_label = Label(fr[3], text="송신 메시지:")
        self.send_btn = Button(fr[3], text="전송", command=self.send_chat)
        self.chat_transcript_area = ScrolledText(fr[2], height=20, width=60)
        self.enter_text_widget = ScrolledText(fr[4], height=5, width=60)
        self.quit_btn = Button(fr[4], text="종료", command=self.close_connection)

        # CtoF 버튼 추가
        self.ctof_btn = Button(fr[4], text="CtoF", command=self.show_ctof_window)

        # 사용자 이름 표시 (수정 불가능)
        self.name_label.pack(side=LEFT, padx=10, pady=10)

        # 수신 및 송신 메시지 구성
        self.recv_label.pack(side=LEFT, padx=10)
        self.chat_transcript_area.pack(side=LEFT, padx=2, pady=2)
        self.send_label.pack(side=LEFT, padx=10)
        self.enter_text_widget.pack(side=LEFT, padx=2, pady=2)

        # 버튼 배치
        self.send_btn.pack(side=RIGHT, padx=20)
        self.quit_btn.pack(side=RIGHT, padx=20, pady=5)
        self.ctof_btn.pack(side=RIGHT, padx=20, pady=5)

    def listen_thread(self):
        '''
        Thread를 생성하고 시작한다
        '''
        t = Thread(target=self.receive_message, args=(self.client_socket,))
        t.start()

    def receive_message(self, so):
        '''
        Server로부터 message를 수신하고 문서창에 표시한다
        '''
        # 빨간색 텍스트 스타일 정의
        self.chat_transcript_area.tag_configure("disconnect", foreground="red")
        self.chat_transcript_area.tag_configure("convert", foreground="blue")
        while True:
            try:
                buf = so.recv(BUFFER_SIZE)
                if not buf:
                    break

                message = buf.decode('utf-8')
                if "(이)가 연결을 종료함." in message:
                    # 연결 종료 메시지를 빨간색으로 표시
                    self.chat_transcript_area.insert('end', message + '\n', "disconnect")
                elif "°F" in message:
                    self.chat_transcript_area.insert('end', message + '\n', "convert")
                else:
                    # 일반 메시지
                    self.chat_transcript_area.insert('end', message + '\n')

                self.chat_transcript_area.yview(END)
            except Exception as e:
                print(f"예외 발생: {e}")
                break
        so.close()

    def show_ctof_window(self):
        '''
        섭씨를 화씨로 변환하는 윈도우를 띄운다
        '''
        self.ctof_window = Toplevel(self.root)
        self.ctof_window.title("섭씨 -> 화씨 변환")

        label = Label(self.ctof_window, text="섭씨 온도를 입력하세요:")
        label.pack(padx=10, pady=5)

        self.celsius_entry = Entry(self.ctof_window)
        self.celsius_entry.pack(padx=10, pady=5)

        convert_btn = Button(self.ctof_window, text="변환", command=self.convert_to_fahrenheit)
        convert_btn.pack(padx=10, pady=5)

        self.result_label = Label(self.ctof_window, text="화씨 온도:")
        self.result_label.pack(padx=10, pady=5)

    def convert_to_fahrenheit(self):
        '''
        섭씨 온도를 화씨로 변환하여 서버로 전송
        '''
        try:
            celsius = float(self.celsius_entry.get())
            fahrenheit = (celsius * 9 / 5) + 32
            self.client_socket.send(f"CTOF:{fahrenheit}".encode('utf-8'))
            self.result_label.config(text=f"화씨 온도: {fahrenheit:.2f}°F")
        except ValueError:
            messagebox.showerror("잘못된 입력", "숫자를 입력해주세요.")

    def close_connection(self):
        '''
        연결 종료 메시지를 서버로 보내고 클라이언트 종료
        '''
        msg = f'사용자 {self.username}(이)가 연결을 종료함.'
        self.client_socket.send(msg.encode('utf-8'))
        self.client_socket.close()
        self.root.quit()

