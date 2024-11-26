'''
실습일: 2024.11.19
실습자: 201910852 심기윤
실습내용: GUI 체팅 클라이언트 실습
'''

# GUI 채팅 클라이언트

from socket import *
from tkinter import *
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText
from threading import *

BUFFER_SIZE = 1024

class ChatClient:
    client_socket = None

    def __init__(self, ip, port):
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
        senders_name = self.name_widget.get().strip()

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
        fr = []
        for i in range(0,5):
            fr.append(Frame(self.root))
            fr[i].pack(fill=BOTH)

        self.name_label = Label(fr[0], text='사용자 이름')
        self.recv_label = Label(fr[1], text = '수신 메시지:')
        self.send_label = Label(fr[3], text = '송신 메시지:')
        self.send_btn = Button(fr[3], text='전송', command=self.send_chat)
        self.chat_transcript_area = ScrolledText(fr[2], height =20, width=60)
        self.enter_text_widget = ScrolledText(fr[4], height =5, width=60)
        self.name_widget = Entry(fr[0], width =15)
        self.quit_btn = Button(fr[4], text='종료', command=self.close_connection)

        self.name_label.pack(side=LEFT)
        self.name_widget.pack(side=LEFT)
        self.recv_label.pack(side=LEFT)
        self.send_btn.pack(side=RIGHT, padx=20)
        self.chat_transcript_area.pack(side=LEFT, padx=2, pady=2)
        self.send_label.pack(side=LEFT)
        self.enter_text_widget.pack(side=LEFT, padx=2, pady=2)
        self.quit_btn.pack(side=RIGHT, padx=20, pady=5)

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
        while True:
            try:
                buf = so.recv(BUFFER_SIZE)
                if not buf:
                    break
                self.chat_transcript_area.insert('end', buf.decode('utf-8') + '\n')
                self.chat_transcript_area.yview(END)
            except ConnectionAbortedError:
                # 연결이 끊어진 경우, 연결 종료 메시지를 출력하고 종료
                print("연결이 종료되었습니다.")
                break
            except Exception as e:
                # 기타 예외 처리
                print(f"예외 발생: {e}")
                break
        so.close()

    def close_connection(self):
        '''
        연결 종료 메시지를 서버로 보내고 클라이언트 종료
        '''
        user = self.name_widget.get().strip()
        msg = f'사용자 {user}가 연결을 종료함.'
        self.client_socket.send(msg.encode('utf-8'))
        self.client_socket.close()
        self.root.quit()


if __name__ == "__main__":
    # ip 매핑
    host = input("서버 IP주소(default=127.0.0.1): ").strip()
    if host == '':
        host = '127.0.0.1'

    # 포트 번호 입력
    port = input("포트 번호(default: 2500): ").strip()
    if port == '':
        port = 2500
    else:
        port = int(port)

    ChatClient(host, port)
    mainloop()
