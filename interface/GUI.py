# Tugas besar 1 IF2211 Strategi Algoritma
# 24 Game Solver menggunakan strategi algoritma greedy
# Anggota Kelompok :
# Winston Wijaya 13517018
# Abda Shaffan Diva 13517021
# Juniardi Akbar 13517075


import PySimpleGUI as sg


def showSelectedImage(path):
    print('masok')
    window.FindElement('_BOX1_').Update(image_filename=path, image_subsample=10, image_size=(350, 350), button_color=sg.TRANSPARENT_BUTTON)
    window.refresh()


window = sg.Window('columns')

# btn1 = sg.FileBrowse( button_text="Open Image", size=(14,1), key="btn1", button_color=('white','#475841'))
btn1 = sg.FileBrowse(file_types=(("Image Files", "*.png"),), button_text="Open Image", size=(14, 1), key="_CHOOSE_",
                     enable_events=True, button_color=('white', '#475841'))
btn2 = sg.Button(button_text="Open Rule Editor", size=(14, 1), key="btn2", button_color=('white', '#475841'))
btn3 = sg.Button(button_text="Show Rules", size=(14, 1), key="btn3", button_color=('white', '#475841'))
btn4 = sg.Button(button_text="Show Facts", size=(14, 1), key="btn4", button_color=('white', '#475841'))
option_layout = [
    [btn1],
    [btn2],
    [btn3],
    [btn4]
]

box1 = sg.Button(image_filename="white.png", image_size=(350, 350), auto_size_button=False,key="_BOX1_", size=(350, 350))
box2 = sg.Image(filename="white.png", key="box2", size=(350, 350))
button_wrapper = sg.Frame(title="Menu", layout=option_layout, size=(50, 50), background_color="#f3f3f3", border_width=0)
box3 = sg.Image(filename="white.png", key="box3", size=(280, 280))
box4 = sg.Image(filename="white.png", key="box4", size=(280, 280))
box5 = sg.Image(filename="white.png", key="box5", size=(280, 280))
layout = [
    [box1, box2, button_wrapper],
    [box3, box4, box5]
]

window = sg.Window('Image Processing', grab_anywhere=True, background_color='#f3f3f3', layout=layout, size=(900, 800))

while True:
    event, values = window.Read()
    # Window Loop Event
    if event is None or event == 'Exit':
        break

    if event == '_CHOOSE_':
        print(values[event])
        showSelectedImage(values[event])

window.Close()
