# 기본 프레임
import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title("JooHeon Lee GUI") # 제목 설정

# 파일 프레임 (파일 축, 선택 삭제)
file_frame = Frame(root)
file_frame.pack()

btn_add_file = Button(file_frame, padx=5, pady=5, width=12, text="파일추가")
btn_add_file.pack(side="left")

btn_del_file = Button(file_frame, padx=5, pady=5, width=12, text="선택삭제")
btn_del_file.pack(side="right")

# 리스트 프레임
list_frame = Frame(root)
list_frame.pack(fill="both")

scrollbar = Scrollbar(list_frame)
scrollbar.pack(side="right", fill="y")

list_file = Listbox(list_frame, selectmode="extended", height=15, yscrollcommand=scrollbar.set)
list_file.pack(side="left", fill="both", expand=True)
scrollbar.config(command=list_file.yview)

# 저장 경로 프레임
path_frame = LabelFrame(root, text="저장경로")
path_frame.pack()

txt_dest_path = Entry(path_frame)
txt_dest_path.pack(side="left", fill="x", expand=True, ipady=4) # 높이변경

btn_dest_path = Button(path_frame, text="찾아보기", width=10)
btn_dest_path.pack(side="right")

# 옵션 프레임
frame_option = LabelFrame(root, text="옵션")
frame_option.pack()

# 1.가로 넓이 옵션

lbl_width = Label(frame_option, text="가로넓이",width=3)
lbl_width.pack(side="left")

# 가로 넓이 콤보
opt_width = ["원본유지", "1024", "800", "640"]
cmb_width = ttk.Combobox(frame_option, state="readonly",  values=opt_width, width=opt_width)
cmb_width.current(0)
cmb_width.pack(side="left")

# 간격 옵션

# 파일 포맷 옵션


root.resizable(False,False) # x(너비), y(높이) 변경 불가
root.mainloop()