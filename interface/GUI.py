import PySimpleGUI as sg

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
    window.FindElement('_BOX1_').Update(image_filename=path, image_subsample=10, image_size=(500, 450), button_color=sg.TRANSPARENT_BUTTON)
    window.refresh()

def showSelectedShape(val):
    window.FindElement('_BOX2_').Update(image_filename="img/"+str(val)+".png", image_subsample=10, image_size=(500, 450), button_color=sg.TRANSPARENT_BUTTON)
    window.refresh()

tree_layout = [[sg.Listbox(values=SHAPES, size=(30, 13), key="_CHOOSESHAPE_", enable_events=True)]]

window = sg.Window('columns')

# btn1 = sg.FileBrowse( button_text="Open Image", size=(14,1), key="btn1", button_color=('white','#475841'))
btn1 = sg.FileBrowse(file_types=(("Image Files", "*.png"),), button_text="Open Image", size=(30,1), key="_CHOOSE_",
                     enable_events=True, button_color=('white', '#475841'))
btn2 = sg.Button(button_text="Open Rule Editor", size=(30,1), key="btn2", button_color=('white', '#475841'))
btn3 = sg.Button(button_text="Show Rules", size=(30,1), key="btn3", button_color=('white', '#475841'))
btn4 = sg.Button(button_text="Show Facts", size=(30,1), key="btn4", button_color=('white', '#475841'))
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

box1 = sg.Button(image_filename="white.png", image_size=(500, 450), auto_size_button=False,key="_BOX1_", size=(500, 450))
box2 = sg.Button(image_filename="white.png", image_size=(500, 450), auto_size_button=False,key="_BOX2_", size=(500, 450))
menu_wrapper = sg.Frame(title="Menu", layout=option_layout, size=(366,450), background_color="#f3f3f3", border_width=0)
box3 = sg.Image(filename="white.png", key="box3", size=(455, 318))
box4 = sg.Image(filename="white.png", key="box4", size=(455, 318))
box5 = sg.Image(filename="white.png", key="box5", size=(455, 318))
layout = [
    [box1, box2, menu_wrapper],
    [box3, box4, box5]
]

window = sg.Window('Image Processing', grab_anywhere=True, background_color='#f3f3f3', layout=layout, size=(1366, 768))

while True:
    event, values = window.Read()
    if event is None or event == 'Exit':
        break

    if event == '_CHOOSE_':
        # print(values[event])
        showSelectedImage(values[event])

    if event == '_CHOOSESHAPE_':
        # print(values[event])

        val = SHAPES.index(values[event][0])
        showSelectedShape(val)

window.Close()
