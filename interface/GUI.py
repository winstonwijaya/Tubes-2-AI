# Tugas besar 1 IF2211 Strategi Algoritma
# 24 Game Solver menggunakan strategi algoritma greedy
# Anggota Kelompok :
# Winston Wijaya 13517018
# Abda Shaffan Diva 13517021
# Juniardi Akbar 13517075


import PySimpleGUI as sg

window = sg.Window('columns')

btn1 = sg.Button(button_text="btn1", size=(10,1), key="btn1")
btn2 = sg.Button(button_text="btn2", size=(10,1), key="btn2")
btn3 = sg.Button(button_text="btn3", size=(10,1), key="btn3")
btn4 = sg.Button(button_text="btn4", size=(10,1), key="btn4")
option_layout = [
    [btn1],
    [btn2],
    [btn3],
    [btn4]
]

box1 = sg.Image(filename="white.png", key="box1", size=(350, 350))
box2 = sg.Image(filename="white.png", key="box2", size=(350, 350))
button_wrapper = sg.Frame(title="Menu", layout=option_layout, size=(30,50), background_color="white")
box3 = sg.Image(filename="white.png", key="box3", size=(280, 280))
box4 = sg.Image(filename="white.png", key="box4", size=(280, 280))
box5 = sg.Image(filename="white.png", key="box5", size=(280, 280))

layout = [
    [box1, box2, button_wrapper],
    [box3, box4, box5]
]

window = sg.Window('Image Processing', grab_anywhere=True, background_color='green', layout=layout, size=(900, 800))

while True:
    event, values = window.Read()
    # Window Loop Event
    if event is None or event == 'Exit':
        break

window.Close()
