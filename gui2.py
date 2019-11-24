import tkinter as tk    
from tkinter import ttk
  
shapes = {
    "Segitiga tidak beraturan" : [
        { "Segitiga lancip" : [] },
        { "Segitiga tumpul" : [] },
        { "Segitiga siku-siku" : [] },
        { "Segitiga sama kaki" : [
            "Segitiga sama kaki dan siku-siku",
            "Segitiga sama kaki dan tumpul",
            "Segitiga sama kaki dan lancip"
        ] },
        { "Segitiga sama sisi" : [] },
    ],
    "Segiempat tidak beraturan" : [
        { "Jajar Genjang" : [
            "Segiempat beraturan",
            "Segiempat berbentuk layang-layang"
        ] },
        { "Trapesium" : [
            "Trapezium sama kaki",
            "Trapezium rata kanan",
            "Trapezium rata kiri"
        ] }
    ],
    "Segi lima tidak beraturan" : [
        { "Segi lima sama sisi" : [] }
    ],
    "Segi enam tidak beraturan" : [
        { "Segi enam sama sisi" : [] }
    ]
}

app = tk.Tk()
app.geometry('1366x786')

top_frame = tk.Frame(app, width=1366, height=393, bg="white")
top_frame.pack(side='top')

source_image = tk.Frame(top_frame, width=500, height=393, bg="salmon")
source_image.grid(row=0, column=0)

detection_image = tk.Frame(top_frame, width=500, height=393, bg="yellow")
detection_image.grid(row=0, column=1)

setting_frame = tk.Frame(top_frame, width=366, height=393, bg="blue")
setting_frame.grid(row=0, column=2)

button_frame = tk.Frame(setting_frame, width=366, height=196, bg="white")
button_frame.pack(side='top')

tree_frame = tk.Frame(setting_frame, width=366, height=196, bg="cyan")
treeview = ttk.Treeview(tree_frame)
for shape in shapes :

    item = treeview.insert("", tk.END, text=shape)
    for subShapes in shapes[shape] :
        for s in subShapes :
            if (len(subShapes[s]) == 0) :
                treeview.insert(item, tk.END, text=s)
            else :
                subitem = treeview.insert(item, tk.END, text=s)
                for x in subShapes[s] :
                    treeview.insert(subitem, tk.END, text=x)
                
    treeview.pack()
tree_frame.pack(side='bottom')

bottom_frame = tk.Frame(app, width=1900, height=393, bg="black")
bottom_frame.pack(side='bottom')

detection_frame = tk.Frame(bottom_frame, width=455, height=393, bg="black")
detection_frame.grid(row=0, column = 0)

matched_frame = tk.Frame(bottom_frame, width=455, height=393, bg="green")
matched_frame.grid(row=0, column = 1)

hit_frame = tk.Frame(bottom_frame, width=455, height=393, bg="red")
hit_frame.grid(row=0, column = 2)


app.mainloop()