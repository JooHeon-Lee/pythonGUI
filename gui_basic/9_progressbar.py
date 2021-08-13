# 프로그래스 바 ( 진행상황 )
import time
import tkinter.ttk as ttk # 콤보박스를 쓰기위한 모듈
from tkinter import *

root = Tk()
root.title("JooHeon Lee GUI") # 제목 설정
root.geometry("640x400")

#progressbar = ttk.Progressbar(root,maximum=100, mode="indeterminate") # 최댓값 지정  indeterminate => 결정되지 않은 상태(언제끝날지모르는작업)
# progressbar = ttk.Progressbar(root,maximum=100, mode="determinate") # 최댓값 지정 determinate => 끝까지 바가 채워짐

# progressbar.start(10) # 10ms 마다 움직임 ( 바 속도)
# progressbar.pack()

# def btncmd():
#   progressbar.stop() # 바 작동 중지

# btn = Button(root, text="중지", command=btncmd)
# btn.pack()

p_var2 = DoubleVar() # 1.2% 20.9% 등등 소수점 발생할수 있기대문에 double
progressbar2 = ttk.Progressbar(root, maximum=100,length=150,variable=p_var2) # length 설정하면 바 가로길이 길게 나옴
progressbar2.pack()

def btncmd2():
    for i in range(1, 101): # 1부터 100까지
        time.sleep(0.01) # 0.01초 대기

        p_var2.set(i) # 0부터 100까지 값을 넣어짐
        progressbar2.update() # ui 업데이트를 하기위해 (시각적으로 보이기 위해) 업데이트
        print(p_var2.get()) # 현재 % 출력
        
btn = Button(root, text="시작", command=btncmd2)
btn.pack()

root.mainloop()