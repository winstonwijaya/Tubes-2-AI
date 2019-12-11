import PySimpleGUI as sg
import os
from imagedetector import *

SHAPES = [
    'Segitiga Lancip',
    'Segitiga Tumpul',
    'Segitiga Siku-siku',
    'Segitiga Sama Kaki dan Siku-siku',
    'Segitiga Sama Kaki dan Tumpul',
    'Segitiga Sama Kaki dan Lancip',
    'Segitiga Sama Sisi',
    'Jajaran Genjang Beraturan',
    'Layang-layang',
    'Trapezium Sama Kaki',
    'Trapezium Rata Kanan',
    'Trapezium Rata Kiri',
    'Segi Lima Sama Sisi',
    'Segi Enam Sama Sisi',
]

def showSelectedImage(path):
    window.FindElement('_BOX1_').Update(image_filename=path, image_subsample=5, image_size=(500, 450),
                                        button_color=sg.TRANSPARENT_BUTTON)
    

    window.refresh()


def showSelectedShape(val):
    root = os.path.abspath("img/" + str(val) + ".png")
    window.FindElement('_BOX2_').Update(image_filename=root, image_subsample=5,
                                        image_size=(500, 450), button_color=sg.TRANSPARENT_BUTTON)
    window.refresh()


tree_layout = [[sg.Listbox(values=SHAPES, size=(30, 13), key="_CHOOSESHAPE_", enable_events=True)]]

window = sg.Window('columns')

label1 = sg.T("Source Image", size=(30, 1), pad=((0, 300), (0, 0)), background_color="#f3f3f3")
label2 = sg.T("Detection Image", size=(30, 1), background_color="#f3f3f3")
label3 = sg.T("Detection Results", size=(30, 1), pad=((0, 250), (0, 0)), background_color="#f3f3f3")
label4 = sg.T("Matched Facts", size=(30, 1), pad=((0, 250), (0, 0)), background_color="#f3f3f3")
label5 = sg.T("Hit Rules", size=(30, 1), pad=((0, 250), (0, 0)), background_color="#f3f3f3")

btn1 = sg.FileBrowse(file_types=(("Image Files", "*.png"),), button_text="Open Image", size=(30, 1), key="_CHOOSE_",
                     enable_events=True, button_color=('white', '#475841'))
btn2 = sg.Button(button_text="Open Rule Editor", size=(30, 1), key="btn2", button_color=('white', '#475841'))
btn3 = sg.Button(button_text="Show Rules", size=(30, 1), key="btn3", button_color=('white', '#475841'))
btn4 = sg.Button(button_text="Show Facts", size=(30, 1), key="btn4", button_color=('white', '#475841'))
button_layout = [
    [btn1],
    [btn2],
    [btn3],
    [btn4]
]

button_wrapper = sg.Frame(title="Menu", layout=button_layout, size=(366, 225), background_color="white")
tree_wrapper = sg.Frame(title="What Shape Do You Want?", layout=tree_layout, size=(366, 225), background_color="white")
option_layout = [
    [button_wrapper],
    [tree_wrapper]
]

box1 = sg.Button(image_filename="white.png", image_size=(500, 450), auto_size_button=False, key="_BOX1_",
                 size=(500, 450), border_width=3)
box2 = sg.Button(image_filename="white.png", image_size=(500, 450), auto_size_button=False, key="_BOX2_",
                 size=(500, 450), border_width=3)
menu_wrapper = sg.Frame(title="", layout=option_layout, size=(366, 450), background_color="#f3f3f3", border_width=0)
box3 = sg.Button(image_filename="white.png", key="_BOX3_", size=(455, 318))
# box4 = sg.Image(filename="white.png", key="box4", size=(455, 318))
box5 = sg.Image(filename="white.png", key="box5", size=(455, 318))
# box3 = sg.Output(size=(60, 50), background_color="#ffffff", key="_RESULTS_")
box4 = sg.Output(size=(60, 50), background_color="#ffffff", key="_FACTS_")
# box5 = sg.Output(size=(60, 50), background_color="#ffffff", key="_RULES_")
layout = [
    [label1, label2],
    [box1, box2, menu_wrapper],
    [label3, label4, label5],
    [box3, box4, box5]
]

window = sg.Window('Image Processing', grab_anywhere=True, background_color='#f3f3f3', layout=layout, size=(1366, 768))

selectedShape = 2

while True:
    event, values = window.Read()
    

    if event is None or event == 'Exit':
        break

    if event == '_CHOOSE_':
        showSelectedImage(values[event])

        image1 = image('image1')
        image1.inputImage(values[event])
        t = image1.findContoursImage()
        fact =  image1.iterateContourInContours(SHAPES[selectedShape])
        print(fact)
        root = os.path.abspath("data-set/hasil.png")
        window.FindElement('_BOX3_').Update(image_filename=root, image_subsample=5,
                                        image_size=(500, 450), button_color=sg.TRANSPARENT_BUTTON)
        window.refresh()


    if event == '_CHOOSESHAPE_':
        val = SHAPES.index(values[event][0])
        selectedShape = val
        showSelectedShape(val)

window.Close()
