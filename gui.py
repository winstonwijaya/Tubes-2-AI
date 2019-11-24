import tkinter as tk
from tkinter import ttk

class Application(ttk.Frame):
    
    def __init__(self, main_window):
        super().__init__(main_window)
        main_window.title("Vista de árbol en Tkinter")
        
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
            ],
        }

        self.treeview = ttk.Treeview(self)

        for shape in shapes :

            item = self.treeview.insert("", tk.END, text=shape)
            self.treeview.bind("<Double-1>", self.OnDoubleClick)

            for subShapes in shapes[shape] :
                for s in subShapes :
                    if (len(subShapes[s]) == 0) :
                        self.treeview.insert(item, tk.END, text=s)
                    else :
                        subitem = self.treeview.insert(item, tk.END, text=s)
                        for x in subShapes[s] :
                            self.treeview.insert(subitem, tk.END, text=x)
                        
            self.treeview.pack()
            
        self.pack()

    def OnDoubleClick(self, event):
        print("you clicked on")

root = tk.Tk()
root.geometry("1300x786")
app = Application(root)
app.mainloop()