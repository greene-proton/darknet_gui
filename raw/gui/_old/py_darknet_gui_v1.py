"""modules"""
import subprocess as sp
import PySimpleGUI as sg
import printdragon as dragon

sg.ChangeLookAndFeel('GreenTan')

layout = [
    #[sg.Text('Project/*.data Name', size=(15, 1)), sg.InputText('Test_name_6')],
    #[sg.Text('Choose Project WS', size=(35, 1))],

    # 0
    [sg.Text('Choose darknet x64 install dir', size=(24, 1), auto_size_text=False, justification='right'),
     sg.InputText('C:/darknet/build/darknet/x64'), sg.FolderBrowse()],

    # 1
    [sg.Text('Choose Project WS', size=(24, 1), auto_size_text=False, justification='right'),
     sg.InputText('C:/darknet/build/darknet/x64/<project>'), sg.FolderBrowse()],

    # 2
    [sg.Text('.data', size=(24, 1), auto_size_text=False, justification='right'),
     sg.InputText('C:/darknet/build/darknet/x64/<project>'), sg.FileBrowse()],

    # 3
    [sg.Text('.cfg', size=(24, 1), auto_size_text=False, justification='right'),
     sg.InputText('C:/darknet/build/darknet/x64/<project>'), sg.FileBrowse()],

    # 4
    [sg.Text('.weights', size=(24, 1), auto_size_text=False, justification='right'),
     sg.InputText('C:/darknet/build/darknet/x64/<project>'), sg.FileBrowse()],

    # 5
    [sg.Text('(for test only) video file', size=(24, 1), auto_size_text=False, justification='right'),
     sg.InputText('C:/darknet/build/darknet/x64/<project>'), sg.FileBrowse()],

    # 6, 7
    [sg.InputCombo(('detector', 'detect', 'demo'), size=(20, 3)),
     sg.InputCombo(('train', 'test'), size=(20, 3))],

    # 8, 9
    [sg.Checkbox('dont_show', default=True), sg.Checkbox('save_labels', default=True)],

    # button
    [sg.Button('TEST GUI'),
     sg.Button('Train'),
     sg.Button('Test with Video'),
     sg.Button('Test'),
     sg.Button('Exit')]
]

window = sg.Window('Darknet YOLOv3 GUI', default_element_size=(100, 2)).Layout(layout)
dragon.print_small_dragon()

while True:
    event, values = window.Read()
    install_dir = values[0]
    project_dir = values[1].replace(install_dir, '')
    data_file = values[2].replace(install_dir, '')
    cfg_file = values[3].replace(install_dir, '')
    weights = values[4].replace(install_dir, '')

    dont_show = values[8]
    save_labels = values[9]

    #print(event, values)
    if event is None or event == 'Exit':
        break
    if event == 'Train':
        if not values[0] or not values[1] or not values[2] or not values[3] or not values[4]:
            sg.Popup('Please fill in directories')
        #window.FindElement('__OUTPUT__').Update(values['__IN__'])
        # sp.call(['darknet.exe', '{}'.format(values[5]), '{}'.format(values[6]),
        #          '{}'.format(values[2].replace(values[0]+'/', '')),
        #          '{}'.format(values[3].replace(values[0]+'/', '')),
        #          '{}'.format(values[4].replace(values[0]+'/', ''))],
        #          cwd='{}'.format(values[0])
        #         )
        else:
            sp.call(['darknet.exe', 'detector', 'train',
                    '{}'.format(data_file),
                    '{}'.format(cfg_file),
                    '{}'.format(weights)],
                    cwd='{}'.format(install_dir)
                    )
            break
    if event == 'Test':
        if not values[0] or not values[1] or not values[2] or not values[3] or not values[4]:
            sg.Popup('Please fill in directories')
        if not save_labels and not dont_show:
            sp.call(['darknet.exe', 'detector', 'test',
                     '{}'.format(data_file),
                     '{}'.format(cfg_file),
                     '{}'.format(weights)],
                    cwd='{}'.format(install_dir)
                    )
            break
        elif save_labels and not dont_show:    
            sp.call(['darknet.exe', 'detector', 'test',
                     '{}'.format(data_file),
                     '{}'.format(cfg_file),
                     '{}'.format(weights)],
                    '-save_labels',
                    '-ext_output',
                    '< {}/data/test.list >'.format(project_dir),
                    '{}/result.txt'.format(project_dir),
                    cwd='{}'.format(install_dir)
                    )
            break
        elif save_labels and dont_show:
            sp.call(['darknet.exe', 'detector', 'test',
                     '{}'.format(data_file),
                     '{}'.format(cfg_file),
                     '{}'.format(weights)],
                    '-dont_show',
                    '-save_labels',
                    '-ext_output',
                    '< {}/data/test.list >'.format(project_dir),
                    '{}/result.txt'.format(project_dir),
                    cwd='{}'.format(install_dir)
                    )
            break
    if event == 'Test with Video':
        sg.Popup('Test with video not yet ready')
    if event == 'TEST GUI':
        if not values[0]:
            sg.Popup('Install Directory Missing!')
        #os.system("start /wait darknet detect cfg/yolov3.cfg yolov3.weights data/dog.jpg")
        else:
            sp.call(['darknet.exe', 'detect', 'cfg/yolov3.cfg', 'yolov3.weights', 'data/dog.jpg'],
                    cwd='{}'.format(values[0])
                    )
            dragon.print_small_dragon()

window.Close()
