from tkinter import filedialog
from PIL import Image, ImageTk

try:
    from tkinter import *
except ImportError:
    import Tkinter as tk


# filename = filedialog.askopenfilename(initialdir = "/",title = "Select Image",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
def choose_image_action(container):
    filename = filedialog.askopenfilename(title="Select Image",
                                          filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))
    print(filename)
    image = PhotoImage(filename)
    image_label = Label(container, image=image)
    image_label.pack()


root = Tk()
root.title("Shape Recognition")
root.configure(width=1300, height=800, background="#f3f3f3")
show_image_frame = Frame(root, width=500, height=500, background='#fff',name="image_frame")
open_image_btn = Button(root, text="Open Image", command=choose_image_action(show_image_frame))
show_image_frame.pack()
open_image_btn.pack()

root.mainloop()
