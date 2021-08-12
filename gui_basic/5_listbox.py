# 텍스트 & 엔트리
from tkinter import *

root = Tk()
root.title("JooHeon Lee GUI") # 제목 설정
root.geometry("640x400")

listbox = Listbox(root, selectmode="extended", height=0) # 한 개 또는 여러개 선택가능
# listbox = Listbox(root, selectmode="single", height=3) # 한개만 선택가능  height는 보여질 갯수 설정하는거임 0 은 전체
listbox.insert(0, "사과")
listbox.insert(1, "딸기")
listbox.insert(2, "바나나")
listbox.insert(END, "수박")
listbox.insert(END, "포도")

listbox.pack()

def btncmd():
   # 삭제
   # listbox.delete(END) # 맨 뒤에 항목 삭제
   # listbox.delete(0) # 맨 앞에 항목 삭제

   # 갯수 확인
   # print("리스트에는",listbox.size(),"개가 있습니다.")

   # 항목 확인 listbox.get(시작인덱스,끝인덱스)
   #print("1번째부터 3번째까지의 항목 : ",listbox.get(0,2)) # 0부터 2까지 출력
   
   # 선택된 항목 확인 (위치로 반환 ex)(1,2,3) )
   print("선택된 항목은 : ",listbox.curselection())

btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop()