tool_id = None
entry1 = None
label_2 = None

import tkinter as tk
import GUI_1 as GUI_1
from tkinter import ttk
import pyodbc
import json
from PIL import Image, ImageTk
import io


# #■■■■■■■■■■■創建伺服器連線■■■■■■■■■■■■■
#以下是使用工坊電腦才適用的參數
# file_path = r"D:\workshop.json"
# with open(file_path) as f:
#     config = json.load(f)

# server = config['SQL_SERVER']
# database = config['SQL_DATABASE']
# username = config['SQL_USERNAME']
# password = config['SQL_PASSWORD']

# conn_str = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}' #把連線資訊存入參數
# conn = pyodbc.connect(conn_str) #使用參數創建連線
#以上是使用工坊電腦才適用的參數

#在微軟的surface的電腦測試用做法
conn = pyodbc.connect("driver={SQL Server};server=DESKTOP-542TC90;database=wokershop;uid=ABC;pwd=12345")  #創建連線

游標 = conn.cursor()    #創建游標

print(游標) #列印游標到螢幕上，確認真的有連線

# #■■■■■■■■■■■段落結束■■■■■■■■■■■■■

def main_Press_button ():
    global tool_id
    tool_id = entry1.get()
    sql_re = GUI_1.print_user_input(tool_id)
    sql_re_1 = sql_re[1]
    sql_re_1 = str(sql_re_1)
    spl_re1 = sql_re_1[:10]
    label_2.config(text=spl_re1)
    #想要讓下面出現照片
    # sql_re_2 = sql_re[2]
    # 第四區塊工具圖片 = io.BytesIO(sql_re_2)
    # 第四區塊工具圖片1 = Image.open (第四區塊工具圖片)
    # 第四區塊工具圖片2 = ImageTk.PhotoImage(第四區塊工具圖片1)
    # label_3 = tk.Label(left_frame,image=第四區塊工具圖片2,width=200,height=200)
    # label_3.pack()

    按下確定要借按鈕()

def 按下確定要借按鈕():
    global tool_id
    Tool_details = GUI_1.print_user_input_1(tool_id) 
    # 清除右側表格中的所有內容
    for row in 右側表格.get_children():
        右側表格.delete(row)

    #將SQL回傳的照片翻譯成圖片
    tool_image = Tool_details[2]
    tool_image_1 = io.BytesIO(tool_image)
    tool_image_2 = Image.open (tool_image_1)
    #tool_image_2.show()
    #tool_image_2.seek(0)
    #tool_image_2.show() #測試是否真的有抓到圖片，秀出來
    # 將圖片對象轉換成 Tkinter 的圖片對象
    tool_image_3 = ImageTk.PhotoImage(tool_image_2)
    
    #使用Canvas顯示圖片
    # canvas= tk.Canvas(右側表格,width=100,height=100)
    # canvas.create_image(0,0,anchor='nw',image=tool_image_3)
    #canvas.pack()


    #print(tool_image_1)
    #print(tool_image_3)
    # image_label = tk.Label(右側表格, image=tool_image_3)
    # image_label.place(relx=0.5, rely=0.8, anchor=tk.CENTER)
    # 將 SQL 查詢結果插入右側表格的新行中
    if Tool_details:
        #右側表格序列 = int(右側表格.index("end")) + 1
        右側表格.insert("", "end", text="",image=tool_image_3, values=( Tool_details[0],  Tool_details[1], tool_image_3))
    else:
    # 如果查詢結果為空，則顯示未找到的消息
        label_2.config(text="未找到相應的工具")


def command_handler():

    # 这里可以添加处理指令的代码

    print("指令已执行")

#def 主程序_按下按鈕(職員編號,entry1,label_2):
    
    
主視窗 = tk.Tk()
主視窗.title("主程序")
主視窗.geometry("1200x800")  # 设置窗口初始大小为1080x1024像素

# ==============创建一个框架作为分隔框的左侧部分==============

left_frame = tk.Frame(主視窗,bg="#F5F5F5",width=480)

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


#button2 = tk.Button(text="確定要借", command=按下確定要借按鈕 )

# 将 Label、Button 和 Entry 放置在主窗口中
label.place(relx=0.12, rely=0.17, anchor=tk.CENTER)
entry1.place(relx=0.12, rely=0.21, anchor=tk.CENTER)
button.place(relx=0.12, rely=0.25, anchor=tk.CENTER)
#button2.place(relx=0.15, rely=0.25, anchor=tk.CENTER)

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

right_frame = tk.Frame(主視窗,bg="white",)

right_frame.pack(side=tk.RIGHT,fill=tk.BOTH,expand=True)

right_frame.propagate(False)
# ==========================================================
style = ttk.Style()
style.configure("Treeview", font=("Arial", 14))


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



