import PySimpleGUI as sg

tree_layout = [[sg.Listbox(values=[
    'Segitiga lancip',
    'Segitiga tumpul',
    'Segitiga siku-siku',
    'Segitiga sama kaki dan siku-siku',
    'Segitiga sama kaki dan tumpul',
    'Segitiga sama kaki dan lancip',
    'Segitiga sama sisi',
    'Jajaran genjang beraturan',
    'Layang-layang',
    'Trapezium sama kaki',
    'Trapezium rata kanan',
    'Trapezium rata kiri',
    'segi lima sama sisi',
    'segi enam sama sisi',
], size=(30, 13))]]

btn1 = sg.Button(button_text="btn1", size=(30,1), key="btn1")
btn3 = sg.Button(button_text="btn3", size=(30,1), key="btn3")
btn4 = sg.Button(button_text="btn4", size=(30,1), key="btn4")
btn2 = sg.Button(button_text="btn2", size=(30,1), key="btn2")
button_layout = [
    [btn1],
    [btn2],
    [btn3],
    [btn4]
]

button_wrapper = sg.Frame(title="Menu", layout=button_layout, size=(366,225), background_color="white")
tree_wrapper = sg.Frame(title="What Shape Do You Want?", layout=tree_layout, size=(366,225), background_color="white")
option_layout = [
    [button_wrapper],
    [tree_wrapper]
]

box1 = sg.Image(filename="white.png", key="box1", size=(500, 450))
box2 = sg.Image(filename="white.png", key="box2", size=(500, 450))
menu_wrapper = sg.Frame(title="", layout=option_layout, size=(366,450), background_color="white")
box3 = sg.Image(filename="white.png", key="box3", size=(455, 318))
box4 = sg.Image(filename="white.png", key="box4", size=(455, 318))
box5 = sg.Image(filename="white.png", key="box5", size=(456, 318))

layout = [
    [box1, box2, menu_wrapper],
    [box3, box4, box5]
]

window = sg.Window('Image Processing', grab_anywhere=True, background_color='green', layout=layout, size=(1366, 768))

while True:
    event, values = window.Read()
    if event is None or event == 'Exit':
        break

window.Close()
