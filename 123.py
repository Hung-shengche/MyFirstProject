import pyodbc
import tkinter as tk
from PIL import Image, ImageTk
import io
import GUI_1 as GUI_1

tool_id = input ('輸入財產編號')
user_input = str(tool_id)  # 獲取使用者輸入的值
BBB = pyodbc.connect("driver={SQL Server};server=DESKTOP-542TC90;database=wokershop;uid=ABC;pwd=12345")
sql_1 = BBB.execute("SELECT * FROM tool where toolID= ?",  (user_input)) #傳入資料庫以供搜尋
print (BBB)
tool_0 = sql_1.fetchone()
tool_1=tool_0[0]
tool_2=tool_0[1]
tool_3=tool_0[2]
print (tool_1,"\n",tool_2,"\n",)


root = tk.Tk()
root.title('oxxo.studio')
root.geometry('400x400')

tool_3 = io.BytesIO(tool_3)
img = Image.open(tool_3)
tk_img = ImageTk.PhotoImage(img)

# label = tk.Label(root, image=tk_img, width=100, height=100, anchor='center')  # 設定 anchor
# label.pack()

canvas = tk.Canvas(root, width=400, height=400)
canvas.create_image(200, 200, anchor='center', image=tk_img)   # 在 Canvas 中放入圖片
canvas.pack()

root.mainloop()
