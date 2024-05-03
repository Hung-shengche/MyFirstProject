import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
<<<<<<< Updated upstream
from tkinter import PhotoImage
import pyodbc
=======
>>>>>>> Stashed changes

root = tk.Tk()
root.title("Treeview with Icons")

# Create Treeview
<<<<<<< Updated upstream
tree = ttk.Treeview(root)
tree.pack()

# Add columns
tree["columns"] = ("名字", "圖標")

# Define column headings
tree.heading("名字", text="名字")
tree.heading("圖標", text="圖標")





img = PhotoImage(file="D:\images.png")
img = img.subsample(4)
tree.insert("","end",text="123",open=True,image=img,values=(1,2))

=======
tree = ttk.Treeview(root,show="headings")
tree.pack()

# Add columns
tree["columns"] = ("Name", "Icon")

# Define column headings
tree.heading("Name", text="Name")
tree.heading("Icon", text="Icon")


# Define sample data (name and image paths)
data = [
    ("電動線鋸機A", "D:\PY\icons\images1.jpg"),
    ("電動線鋸機B", "D:\PY\icons\images1.jpg"),
    ("電動線鋸機C", "D:\PY\icons\images1.jpg")
]

# Load icons and add them to Treeview
icons = {}
for name, path in data:
    # Load image and resize if necessary
    img = Image.open(path)
    img = img.resize((24, 24) )  # Resize image as needed
    icon = ImageTk.PhotoImage(img)
    icons[name] = icon  # Save icon reference for later use
    # Insert item with icon into Treeview
    tree.insert("", "end", text=name, values=(name, icon))
>>>>>>> Stashed changes

root.mainloop()
