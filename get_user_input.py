import tkinter as tk

def get_user_input(entry):
    user_input = entry.get()  # 獲取使用者輸入的值
    # 在這裡執行將使用者輸入的值發送到 SQL 中進行搜索的操作