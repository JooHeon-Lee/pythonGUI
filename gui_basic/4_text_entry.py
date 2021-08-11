# 텍스트 & 엔트리
from tkinter import *

root = Tk()
root.title("JooHeon Lee GUI") # 제목 설정
root.geometry("640x400")

txt = Text(root, width=30, height=5)
txt.pack()
txt.insert(END,"글자를 입력하세요")

e = Entry(root, width=30) # 엔트리는 엔터입력 불가 한줄로 입력받을떄 사용
e.pack()
e.insert(0,"한 줄만 입력해요") #기본값 세팅

def btncmd():
    #내용 가져오기
    print(txt.get("1.0",END)) # 처음부터 끝까지 모든 텍스트를 가져옴 1.0에서 1은 라인1부터가져와라 0은 칼럼기준으로 0번째부터 가져와라
    print(e.get())

    #내용삭제
    txt.delete("1.0",END)
    e.delete(0,END)

btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop()