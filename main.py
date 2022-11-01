from tkinter import *
from tkinter import messagebox
import socket

root = Tk()
root.title("EazyOrder Server") #창 이름 지정
root.attributes('-fullscreen',True)
root.resizable(False, False) #해상도 변경 불가

##############여기부터 함수##############

def open_store():
    btn1.pack_forget()
    messagebox.showinfo("알림", "개점 처리되었습니다")

##############여기부터 GUI##############
btn1 = Button(root, text="개점처리", command=open_store)
btn1.pack()


root.mainloop()