import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

root = tk.Tk()
root.title("Treeview with Icons")

# Create Treeview
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

root.mainloop()
