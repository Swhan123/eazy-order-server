from tkinter import *
from tkinter import messagebox
import socket, threading
import os

root = Tk()
root.title("EazyOrder Server") #창 이름 지정
root.attributes('-fullscreen',True)
root.resizable(False, False) #해상도 변경 불가



##############여기부터 변수##############


##############여기부터 함수##############

def setting():
    btn1.pack_forget()
    textbox.pack(padx=10, pady=10)
    textbox.place(x=1, y=1)
    btn2.pack()
    btn2.place(x=1, y=100)
    

def binder(client_socket, addr):
    # 커넥션이 되면 접속 주소가 나온다.
    print('Connected by', addr)
    try:
        while True:
            # 1024byte 이하의 데이터 수신
            data = client_socket.recv(1024)
            msg = data.decode()
            # 수신된 메시지를 콘솔에 출력한다.
            msg = "echo : " + msg
            data = msg.encode()
            length = len(data)
            client_socket.sendall(length.to_bytes(1024, byteorder="little"))
            # 데이터를 클라이언트로 전송한다.
            client_socket.sendall(data)
    except:
    # 접속 해제시 except
        print("except : " , addr)
    finally:
    # 종료
        client_socket.close()



def open_store():
    btn1.pack_forget()
    # 커넥션이 되면 접속 주소가 나온다.
    messagebox.showinfo("알림", "클라이언트 응답 대기중 입니다. 클라이언트에서 이지오더 프로그램을 실행해 주세요.")

    # 소켓 생성
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # 10000번 포트 사용
    server_socket.bind(('',10000))

    server_socket.listen(1)

    try:
        # 클라이언트가 접속하기 전까지 서버는 실행되야하기 때문에 무한 루프 사용
        while True:
            client_socket, addr = server_socket.accept()
        # 쓰레드 사용해서 대기
            th = threading.Thread(target=binder, args = (client_socket,addr))
            th.start()
    except:
        print("server")
    finally:
        # 종료
        server_socket.close()

def printstr():
    btn2.pack()

def writename():
    print('여기부터')
##############여기부터 GUI##############


btn1 = Button(root, text="개점처리", width=20, height=3, command=open_store)
btn1.pack()

str = StringVar()
textbox = Entry(root,  width=20, textvariable=str)
btn2 = Button(root, text="매장 이름 설정하기", width=20, height=3, command=writename)

if os.path.isfile("settings.txt") == False:
    setting()

root.mainloop()