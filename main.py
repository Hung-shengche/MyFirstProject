tool_id = None
entry1 = None
entry2 = None
entry3 = None
label_2 = None


import tkinter as tk
import GUI_1 as GUI_1
from tkinter import ttk
import pyodbc
import json
from PIL import Image, ImageTk
import io
from tkinter import PhotoImage

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
#在家中四樓的電腦測試用作法
#conn = pyodbc.connect("driver={SQL Server};server=DESKTOP-PSC83VE;database=workshop;uid=ABC;pwd=12345") 
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
    tool_image_data = sql_re[2]
    tool_image = Image.open(io.BytesIO(tool_image_data))
    tool_photo = ImageTk.PhotoImage(tool_image)
    canvas1.create_image(0, 0, anchor=tk.NW, image=tool_photo)
    canvas1.image = tool_photo
    # label_3 = tk.Label(left_frame,image=第四區塊工具圖片2,width=200,height=200)                                                                                  
    # label_3.pack()
    按下確定要借按鈕()

def main_Press_學號欄():
    global entry2 
    student_id = entry2.get()
    sql_re_s = GUI_1.print_user_input_2(student_id)
    if sql_re_s is None:
        print ("None")
        
    else :
        學生學號 = str(sql_re_s[0])
        學生學號 = 學生學號[:9]
        學生姓名 = str(sql_re_s[1])
        學生姓名 = 學生姓名[:3]
        學生電話 = str(sql_re_s[2])
        學生電話 = 學生電話[:10]
        print(學生學號,學生姓名,學生電話)
    


def 按下確定要借按鈕():
    global tool_id
    Tool_details = GUI_1.print_user_input_1(tool_id) 
    # 清除右側表格中的所有內容
    for row in 右側表格.get_children():
        右側表格.delete(row)

    #將SQL回傳的照片翻譯成圖片
    # tool_image = Tool_details[2]
    # tool_image_1 = io.BytesIO(tool_image)
    # tool_image_2 = Image.open (tool_image_1)
    # tool_image_3 = ImageTk.PhotoImage(tool_image_2)

    #工具狀態欄
    tool_state = Tool_details[4]


    # 將 SQL 查詢結果插入右側表格的新行中
    if Tool_details:
        #右側表格序列 = int(右側表格.index("end")) + 1
        if tool_state is True:
            on_lend = "出借中"
        else :
            on_lend = "在庫"

        右側表格.insert("", "end", text="", values=(Tool_details[0],  Tool_details[1], on_lend ))
    else:
    # 如果查詢結果為空，則顯示未找到的消息
        label_2.config(text="未找到相應的工具")


def command_handler():

    # 这里可以添加处理指令的代码

    print("指令已执行")

#def 主程序_按下按鈕(職員編號,entry1,label_2):
    
    
主視窗 = tk.Tk()
主視窗.title("主程序")
主視窗.geometry("1080x680")  # 设置窗口初始大小为1080x680像素

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

#==============創建輸入財產編號區塊
label = tk.Label(text="掃描工具條碼或手打財編",font=("SimSun", 12))
entry1 = tk.Entry()  # 创建一號输入框
職員編號 = entry1.get()  # 獲取使用者輸入的值
button = tk.Button(text="用財產編號查看", command=main_Press_button)


#button_還 = tk.Button(text="還這個工具", command=按下確定要借按鈕 )

# 将 Label、Button 和 Entry 放置在主窗口中
label.place(relx=0.12, rely=0.17, anchor=tk.CENTER)
entry1.place(relx=0.12, rely=0.21, anchor=tk.CENTER)
button.place(relx=0.26, rely=0.20, anchor=tk.CENTER)
#button_還.place(relx=0.15, rely=0.25, anchor=tk.CENTER)

# 綁定按下 Enter 鍵觸發按鈕事件
主視窗.bind('<Return>', main_Press_button)


#==============創建輸入學生證號區塊
label = tk.Label(text="掃描學生證或手打學號",font=("SimSun", 12))
entry2 = tk.Entry()  # 创建二號输入框
學號欄 = entry2.get()  # 獲取使用者輸入的值
button = tk.Button(text="用學生學號查看", command=main_Press_學號欄)

# 将 Label、Button 和 Entry 放置在主窗口中
label.place(relx=0.12, rely=0.31, anchor=tk.CENTER)
entry2.place(relx=0.12, rely=0.35, anchor=tk.CENTER)
button.place(relx=0.26, rely=0.25, anchor=tk.CENTER)


#==============建立手機號碼輸入區塊

label = tk.Label(text="請輸入聯絡手機",font=("SimSun", 12))
entry3 = tk.Entry()  # 创建三號输入框
連絡電話 = entry3.get()  # 獲取使用者輸入的值
button = tk.Button(text="用手機號碼查看", command=GUI_1.print_user_input)
非必填 = tk.Label(text="(非必填)",font=("SimSun", 9))
# 将 Label、Button 和 Entry 放置在主窗口中
label.place(relx=0.12, rely=0.45, anchor=tk.CENTER)
entry3.place(relx=0.12, rely=0.48, anchor=tk.CENTER)
button.place(relx=0.26, rely=0.30, anchor=tk.CENTER)
非必填.place(relx=0.12, rely=0.51, anchor=tk.CENTER)                                                                               
#==============建立第四區塊

label = tk.Label(text="搜尋結果",font=("微軟正黑體", 12))
label_2 = tk.Label(font=(14))
label.place(relx=0.12, rely=0.57, anchor=tk.CENTER)
label_2.place(relx=0.12, rely=0.62, anchor=tk.CENTER)
canvas1 = tk.Canvas(width=200, height=200)
canvas1.place(relx=0.12, rely=0.80, anchor=tk.CENTER)

#==============按鈕區塊

列出所有出借中的工具 = tk.Entry()  # 创建三號输入框
所有出借中工具 = 列出所有出借中的工具.get()  # 獲取使用者輸入的值
列出所有工具按鈕 = tk.Button(text="列出所有出借中工具", command=GUI_1.print_user_input)
列出所有工具按鈕.place(relx=0.26, rely=0.35, anchor=tk.CENTER)

列出所有在庫工具 = tk.Entry()  # 创建三號输入框
所有在庫工具 = 列出所有在庫工具.get()  # 獲取使用者輸入的值
列出在庫工具按鈕 = tk.Button(text="列出所有在庫的工具", command=GUI_1.print_user_input)
列出在庫工具按鈕.place(relx=0.26, rely=0.40, anchor=tk.CENTER)

該工具出借紀錄 = tk.Entry()  # 创建三號输入框
列出該工具的出借紀錄 = 該工具出借紀錄.get()  # 獲取使用者輸入的值
工具出借紀錄 = tk.Button(text="列出該工具的出借紀錄", command=GUI_1.print_user_input)
工具出借紀錄.place(relx=0.26, rely=0.45, anchor=tk.CENTER)

該學生借用紀錄 = tk.Entry()  # 创建三號输入框
列出該學生的借用紀錄 = 該學生借用紀錄.get()  # 獲取使用者輸入的值
學生借用紀錄 = tk.Button(text="列出該學生的借用紀錄", command=GUI_1.print_user_input)
學生借用紀錄.place(relx=0.26, rely=0.50, anchor=tk.CENTER)

確定借 = tk.Entry()  # 创建三號输入框
學生要借 = 確定借.get()  # 獲取使用者輸入的值
學生借用工具 = tk.Button(text="要借該工具",bg="red", command=GUI_1.print_user_input)
學生借用工具.place(relx=0.26, rely=0.55, anchor=tk.CENTER)

要還的 = tk.Entry()  # 创建三號输入框
學生要還 = 要還的.get()  # 獲取使用者輸入的值
學生要還工具 = tk.Button(text="要來還工具",bg="green", command=GUI_1.print_user_input)
學生要還工具.place(relx=0.26, rely=0.60, anchor=tk.CENTER)

新工具 = tk.Entry()  # 创建三號输入框
創建工具 = 新工具.get()  # 獲取使用者輸入的值
創建新工具 = tk.Button(text="創建新工具", command=GUI_1.print_user_input)
創建新工具.place(relx=0.26, rely=0.65, anchor=tk.CENTER)
# ==============创建一个框架作为分隔框的右侧部分==============

#●○●○●○●○●○●○●○●○●○最基本的顯示環境，看能不能顯示圖片●○●○●○●○●○●○●○
# L_tree = ttk.Treeview(主視窗)
# L_tree.pack(side=tk.RIGHT,fill=tk.BOTH,expand=True)

# # Add columns
# L_tree["columns"] = ("名字", "圖標")

# # Define column headings
# L_tree.heading("名字", text="名字")
# L_tree.heading("圖標", text="圖標")

# img = PhotoImage(file="D:\images.png")
# img = img.subsample(4)
# L_tree.insert("","end",text="123",open=True,image=img,values=(1,2))

# L_tree.mainloop()

#●○●○●○●○●○●○●○●○●○最基本的顯示環境，看能不能顯示圖片●○●○●○●○●○●○●○結束



right_frame = tk.Frame(主視窗,bg="white",)

right_frame.pack(side=tk.RIGHT,fill=tk.BOTH,expand=True)

right_frame.propagate(False)
# ==========================================================
style = ttk.Style()
style.configure("Treeview", font=("微軟正黑體", 12))


右側表格 = ttk.Treeview(right_frame,columns=("第一列","第二列","第三列"),show="headings")

#右側表格.heading("#0",text="序列")

右側表格.heading("#1",text="工具財編")

右側表格.heading("#2",text="工具名稱")

右側表格.heading("#3",text="目前狀態")

# 设置列宽度

#右側表格.column("#0",width=200)

# 布局Treeview

右側表格.pack(expand=True,fill="both")


主視窗.mainloop()



