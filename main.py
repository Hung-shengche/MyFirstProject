tool_id = None
entry1 = None
label_2 = None

import tkinter as tk
import GUI_1 as GUI_1
from tkinter import ttk
import pyodbc
import json

# #■■■■■■■■■■■創建伺服器連線■■■■■■■■■■■■■

file_path = r"D:\workshop.json"
with open(file_path) as f:
    config = json.load(f)

# 获取连接参数
server = config['SQL_SERVER']
database = config['SQL_DATABASE']
username = config['SQL_USERNAME']
password = config['SQL_PASSWORD']

conn_str = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}' #把連線資訊存入參數
conn = pyodbc.connect(conn_str) #使用參數創建連線

#連線 = pyodbc.connect("driver={SQL Server};server=DESKTOP-GMC9JU6\SQLEXPRESS_HUNG;database=workshop;uid=workshop_worker;pwd=work2024")  #創建連線

AAA = conn.cursor()    #創建游標

print(AAA) #列印游標到螢幕上，確認真的有連線

# #■■■■■■■■■■■段落結束■■■■■■■■■■■■■

def main_Press_button (AAA,event=None):
    global tool_id
    tool_id = entry1.get()
    sql_re = GUI_1.print_user_input(AAA,tool_id)
    
    label_2.config(text=sql_re)


def command_handler():

    # 这里可以添加处理指令的代码

    print("指令已执行")

#def 主程序_按下按鈕(職員編號,entry1,label_2):
    
    
主視窗 = tk.Tk()
主視窗.title("主程序")
主視窗.geometry("1200x800")  # 设置窗口初始大小为1080x1024像素

# ==============创建一个框架作为分隔框的左侧部分==============

left_frame = tk.Frame(主視窗,bg="#F5F5F5",width=360)

left_frame.pack(side=tk.LEFT,fill=tk.BOTH,expand=False)

left_frame.propagate(False)
# ==========================================================

#==============創建第零個區塊
label = tk.Label(text="來工坊借工具", font=("Arial", 18))
label_1 = tk.Label(text="程式設計:洪聖哲", font=("SimSun", 12))

label.place(relx=0.12, rely=0.03, anchor=tk.CENTER)
label_1.place(relx=0.16, rely=0.09, anchor=tk.CENTER)

#==============創建第一個區塊
label = tk.Label(text="掃描工具條碼或手打財編",font=( 14))
entry1 = tk.Entry()  # 创建一號输入框
職員編號 = entry1.get()  # 獲取使用者輸入的值
button = tk.Button(text="执行操作", command=main_Press_button)


# 将 Label、Button 和 Entry 放置在主窗口中
label.place(relx=0.12, rely=0.17, anchor=tk.CENTER)
entry1.place(relx=0.12, rely=0.21, anchor=tk.CENTER)
button.place(relx=0.12, rely=0.25, anchor=tk.CENTER)

# 綁定按下 Enter 鍵觸發按鈕事件
主視窗.bind('<Return>', main_Press_button)


#==============創建第二個區塊
label = tk.Label(text="掃描學生證或手打學號",font=( 14))
entry2 = tk.Entry()  # 创建二號输入框
user_input = entry2.get()  # 獲取使用者輸入的值
button = tk.Button(text="执行操作", command=GUI_1.print_user_input)

# 将 Label、Button 和 Entry 放置在主窗口中
label.place(relx=0.12, rely=0.31, anchor=tk.CENTER)
entry2.place(relx=0.12, rely=0.35, anchor=tk.CENTER)
button.place(relx=0.12, rely=0.39, anchor=tk.CENTER)


#==============建立第三區塊

label = tk.Label(text="請輸入聯絡手機",font=( 14))
entry3 = tk.Entry()  # 创建三號输入框
user_input = entry3.get()  # 獲取使用者輸入的值
button = tk.Button(text="执行操作", command=GUI_1.print_user_input)

# 将 Label、Button 和 Entry 放置在主窗口中
label.place(relx=0.12, rely=0.45, anchor=tk.CENTER)
entry3.place(relx=0.12, rely=0.48, anchor=tk.CENTER)
button.place(relx=0.12, rely=0.51, anchor=tk.CENTER)

#==============建立第四區塊

label = tk.Label(text="搜尋結果",font=( 14))
label_2 = tk.Label(font=(14))
label.place(relx=0.12, rely=0.57, anchor=tk.CENTER)
label_2.place(relx=0.12, rely=0.60, anchor=tk.CENTER)
# gui1 = GUI_1.GUI_a()

# gui2 = GUI_1.GUI_b(職員編號)

# gui3 = GUI_1.GUI_c()

# ==============创建一个框架作为分隔框的右侧部分==============

right_frame = tk.Frame(主視窗,bg="white")

right_frame.pack(side=tk.RIGHT,fill=tk.BOTH,expand=True)

right_frame.propagate(False)
# ==========================================================



右側表格 = ttk.Treeview(right_frame,columns=("第一列","第二列","第三列"))

右側表格.heading("#0",text="序列")

右側表格.heading("#1",text="工具財編")

右側表格.heading("#2",text="工具名稱")

右側表格.heading("#3",text="工具圖片")

# 设置列宽度

右側表格.column("#0",width=80)

# 布局Treeview

右側表格.pack(expand=True,fill="both")


主視窗.mainloop()



