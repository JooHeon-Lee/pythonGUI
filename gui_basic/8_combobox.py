# 콤보박스
# height 는 보여지는 갯수
import tkinter.ttk as ttk # 콤보박스를 쓰기위한 모듈
from tkinter import *

root = Tk()
root.title("JooHeon Lee GUI") # 제목 설정
root.geometry("640x400")

values = [str(i) + "일" for i in range(1, 32)]

combobox = ttk.Combobox(root, height=5, values=values)
combobox.pack()
combobox.set("카드 결제일") # 최초 목록 제목 및 버튼클릭을 통한 값설정 가능


readonly_combobox = ttk.Combobox(root, height=10, values=values,state="readonly") # readonly 설정
readonly_combobox.current(0)
readonly_combobox.pack()


def btncmd():
   print(combobox.get()) # 선택된 값 출력
   print(readonly_combobox.get())

btn = Button(root, text="선택", command=btncmd)
btn.pack()

root.mainloop()