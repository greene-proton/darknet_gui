"""modules"""
#import os
import PySimpleGUI as sg
import gui.py_darknet_gui_class_v1 as gui_1
import gui.printdragon as kiwi

sg.ChangeLookAndFeel('GreenTan')
GUI_1 = gui_1.YOLOv3MainGUI()

kiwi.print_green_kiwi()

while True:
    layout = [
        # button
        [#sg.Button('pause test'),
         sg.Button('Darknet')],

        [sg.Button('Exit')]
    ]
    window = sg.Window('Darknet YOLOv3 GUI', default_element_size=(100, 2)).Layout(layout)
    event, values = window.Read()

    if event is None or event == 'Exit':
        break

    if event == 'Darknet':
        window.Close()
        GUI_1.init_darknet_gui()

window.Close()
