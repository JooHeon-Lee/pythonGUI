# 기본 프레임
from tkinter import *

root = Tk()
root.title("JooHeon Lee GUI") # 제목 설정

btn1 = Button(root, text="버튼1")
btn1.pack() # pack을 호출해줘야 메인 윈도우에 포함됨

btn2 = Button(root, padx=5, pady=10, text="버튼2") # padx = 좌우공간(여백) pady = 상하공간  내용이 많아지면 버튼도 커짐
btn2.pack()

btn3 = Button(root, padx=10, pady=5, text="버튼3")
btn3.pack()

btn4 = Button(root, width=10, height=5, text="버튼4") # 내용이 많으면 크기는 안변하고 글자가 잘림
btn4.pack()

btn5 = Button(root, fg="red", bg="yellow", text="버튼5")
btn5.pack()

photo = PhotoImage(file="gui_basic/btnImg.png") # 이미지로 버튼 생성
btn6 = Button(root,image=photo)
btn6.pack()

def btncmd():
    print("버튼이 클릭되었어요")

btn7 = Button(root, text="동작 하는 버튼", command=btncmd)
btn7.pack()

root.mainloop()