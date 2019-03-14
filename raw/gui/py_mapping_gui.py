"""modules"""
import os
import PySimpleGUI as sg
import gui.printdragon as kiwi
import src.py_src_main as start

class MappingGUI():
    """class MappingGUI()"""
    static_array = []
    def __init__(self):
        self.dyn_array = []
        self.layout = []
    
    def init_gui_2_layout(self):
        """def init_gui_2_layout(self)"""
        layout = [
            #[sg.Text('Project/*.data Name', size=(15, 1)), sg.InputText('Test_name_6')],
            #[sg.Text('Choose Project WS', size=(35, 1))],

            # 0
#            [sg.Text('Choose darknet x64 install dir', size=(24, 1), auto_size_text=False, justification='right'),
#             sg.InputText('C:/darknet/build/darknet/x64'), sg.FolderBrowse()],

            # 1
#            [sg.Text('Choose Project WS', size=(24, 1), auto_size_text=False, justification='right'),
#             sg.InputText('C:/darknet/build/darknet/x64/<project>'), sg.FolderBrowse()],

            # 2
            [sg.Text('Ortho image directory', size=(24, 1), auto_size_text=False, justification='right'),
             sg.InputText('C:/darknet/build/darknet/x64/<project>'), sg.FileBrowse()],

            # 3
            [sg.Text('Save data results', size=(24, 1), auto_size_text=False, justification='right'),
             sg.InputText('C:/darknet/build/darknet/x64/<project>'), sg.FileBrowse()],
            


            # button
            [sg.Button('Start'),
             sg.Button('Exit')]
        ]
        kiwi.print_green_kiwi()
        return sg.Window('Darknet YOLOv3 GUI', default_element_size=(100, 2)).Layout(layout)

    def run_gui_2(self):
        """init_gui2_main"""
        sg.ChangeLookAndFeel('GreenTan')
        while True:
            window = self.init_gui_2_layout()
            event, values = window.Read()
            if window is None or event == 'Exit':
                break

            # install_dir = values[0]+'/'
            # project_dir = values[1]+'/'
            image_folder_dir = values[0]+'/'
            save_res_dir = values[1]+'/'

            if event == 'Start':
                window.Close()
                if os.path.isdir(save_res_dir):
                    sg.Popup(
                        '{}/test_filtered_shp.shp.kml'.format(save_res_dir),
                        '{}/test_hex_heatMap.shp.kml'.format(save_res_dir)
                        )
                    start.start_analysis(image_folder_dir, save_res_dir)
                else:
                    sg.Popup(
                        'No such directory:\n{}'.format(save_res_dir)
                        )
        window.Close()
