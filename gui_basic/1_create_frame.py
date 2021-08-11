# 기본 프레임
from tkinter import *

root = Tk()
root.title("JooHeon Lee GUI") # 제목 설정
root.geometry("640x480") # 가로 x 세로 크기 지정
# root.geometry("640x480+300+100") # 가로 x 세로 + x좌표 + y좌표

root.resizable(False,False) # x(너비), y(높이) 변경 불가


root.mainloop()