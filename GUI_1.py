import tkinter as tk
#import GUI_1 as gui_def
import pyodbc
import json



# def GUI_a():
#     label = tk.Label(text="來跟阿哲借工具", font=("Arial", 18))
#     label_1 = tk.Label(text="程式設計:洪聖哲", font=("SimSun", 12))

#     label.place(relx=0.12, rely=0.03, anchor=tk.CENTER)
#     label_1.place(relx=0.16, rely=0.09, anchor=tk.CENTER)


def print_user_input(tool_id): #把工具財產編號傳入SQL搜尋並回傳
    
    user_input = str(tool_id)  # 獲取使用者輸入的值
    BBB = pyodbc.connect("driver={SQL Server};server=DESKTOP-542TC90;database=wokershop;uid=ABC;pwd=12345")
    sql_1 = BBB.execute("SELECT * FROM tool where toolID= ?",  (user_input,)) #傳入資料庫以供搜尋
    tool_0 = sql_1.fetchone()
    # print(tool_1)
    # #BBB.close()
    # return tool_1
    if tool_0:
        #tool_1=tool_0[1]
        #print(tool_0)
        BBB.close()
        return tool_0
    else :
        BBB.close()
        return None
    
def print_user_input_1(tool_id): #把工具財編搜尋過之後出現在右側
    
    user_input = str(tool_id)  # 獲取使用者輸入的值
    CCC = pyodbc.connect("driver={SQL Server};server=DESKTOP-542TC90;database=wokershop;uid=ABC;pwd=12345")
    sql_2 = CCC.execute("SELECT * FROM tool where toolID= ?",  (user_input,)) #傳入資料庫以供搜尋
    工具細項 = sql_2.fetchone()
    CCC.close
    return 工具細項


# def GUI_b(職員編號):

#     #global entry  # 使用全局變數 entry
#     label = tk.Label(text="掃描學生證或手打學號",font=( 14))
#     entry = tk.Entry()  # 创建一个输入框
#     user_input = entry.get()  # 獲取使用者輸入的值
#     button = tk.Button(text="执行操作", command=print_user_input)
    

#     # 将 Label、Button 和 Entry 放置在主窗口中
#     label.place(relx=0.1, rely=0.17, anchor=tk.CENTER)
#     entry.place(relx=0.1, rely=0.19, anchor=tk.CENTER)
#     button.place(relx=0.1, rely=0.23, anchor=tk.CENTER)
        
# def GUI_c ():
#     global entry  # 使用全局變數 entry2
#     label2 = tk.Label(text="掃描工具條碼或手打財編",font=( 14))
#     entry = tk.Entry()  # 创建一个输入框
#     user_input = entry.get()  # 獲取使用者輸入的值
#     button = tk.Button(text="执行操作", command=print_user_input)
    

#     # 将 Label、Button 和 Entry 放置在主窗口中
#     label2.place(relx=0.1, rely=0.30, anchor=tk.CENTER)
#     entry.place(relx=0.1, rely=0.32, anchor=tk.CENTER)
#     button.place(relx=0.1, rely=0.35, anchor=tk.CENTER)


# def 主程序_按下按鈕():
#     global 職員編號
#     職員編號 = entry1.get()
#     資料庫搜尋結果 = GUI_1.print_user_input(職員編號)
#     label_2.config(text=資料庫搜尋結果)
