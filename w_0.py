
import tkinter as tk

from tkinter import ttk

# import 試算表_2 as 試算表




def command_handler():

    # 这里可以添加处理指令的代码

    print("指令已执行")

# 创建主窗口

主視窗 = tk.Tk()

主視窗.title("分隔框示例")


# 设置窗口大小为 1080x1024

主視窗.geometry("1080x800")


# 创建一个框架作为分隔框的左侧部分

left_frame = tk.Frame(主視窗,bg="light gray",width=360)

left_frame.pack(side=tk.LEFT,fill=tk.BOTH,expand=False)

left_frame.propagate(False)


# 创建一个框架作为分隔框的右侧部分

right_frame = tk.Frame(主視窗,bg="white")

right_frame.pack(side=tk.RIGHT,fill=tk.BOTH,expand=True)

right_frame.propagate(False)



右側表格 = ttk.Treeview(right_frame,columns=("第一列","第二列","第三列"))



右側表格.heading("#0",text="序列")

右側表格.heading("#1",text="工具財編")

右側表格.heading("#2",text="工具名稱")

右側表格.heading("#3",text="工具圖片")




# 设置列宽度

右側表格.column("#0",width=100)




# 布局Treeview

右側表格.pack(expand=True,fill="both")






# 在左侧部分的框架中添加一个按钮来执行指令

button = tk.Button(left_frame,text="执行指令",command=command_handler)

button.pack(padx=20,pady=20)




# 在右侧部分的框架中添加一个按钮来执行指令

button = tk.Button(right_frame,text="执行指令",command=command_handler)

button.pack(padx=20,pady=20)




# 运行主循环

主視窗.mainloop()