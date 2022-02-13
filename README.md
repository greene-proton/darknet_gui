# darknet_gui
simple standalone gui for YOLOv3 darknet. This specifically makes use of [darknet](https://github.com/AlexeyAB/darknet/) forked by AlexeyAB  for windows install. There are certainly better GUIs out there for YOLO and this is one is mainly for personal use.

## Install
- Install darknet YOLOv3 for windows ([darknet](https://github.com/AlexeyAB/darknet/))
- Add darknet install directory to `Path` in System variables
  - add a new variable under `Path`, where the variable is the path where `./darknet.exe` is installed
    - This may look something like `C:\darknet\build_win_release\Release` or `C:\dev\_ws\darknet\build\darknet\x64` depending on how you've installed darknet. 
  - See steps 1 - 5 in this link if you are new to adding paths to system variables: [add-path-environment-variables](https://docs.telerik.com/teststudio/features/test-runners/add-path-environment-variables)
- use `git clone` or direct download, then unzip to preferred directory.

## Usage
- run `py_main_gui.exe`
- Use `TEST GUI` with correct install directory of darknet x64 in the first field (ie. `C:/.../darknet/build/darknet/x64`)
  - This will just run the following commandline as a self test to check that the ui is working correctly:
  ```
  darknet.exe detector test cfg/coco.data yolov3.cfg yolov3.weights -ext_output dog.jpg
  ```
- Use the `Train` button to start dataset with correct directories to `*.data` `*.cfg` and `*.weights` (use `darknet53.conv.74` if new model). See file structure below. 
- The `create *.list` and `Make *.list for pseudo labeling` buttons assumes the following files structure:
```
.../x64/
       /<project workspace>/
                           /data/
                                /test/(store images and labels for testing)
                                /train/(store images and labels for training)
                                /new_train/(store images to be auto labeled by trained model)
```
- `create *.list` looks into your project workspace, under the x64 darknet build, and looks through image file types (.png and .jpg) nested in data/train/ and data/test/ to make `train.list` and `test.list`. 

## Change Log
### R01.010 (Planned/Todo List)
- `mAP analysis` window from main menu. 
  - Scan though all .weights file in a folder and create a plot for average precision (AP), recall, f-1 score and mean AP (mAP)
### R01.006 (minor fix)
- Added caps check for `.jpg` and `.png` in `create list` functions.
### R01.005
- Added `Make pseudo label`
  - populate test folder with `*.txt` labels (this will replace labels already previously saved in that folder) 
- Added `Test w/ Image` 
  - Just detection on single image of you choosing 
- Added `save video function`
  - save test demo video as same directory as video as `<test_vid_name>_res.avi`
### R01.004
- Fixed random crashes when pressing buttons (most if not all loop issues)
- updated `Test` button to `mAP Test`. 
- updated `Test /w video` and `Test /w Webcam`
- Fixed some crashes caused by _tkinter.TclError
### R01.003
- added `create *.list` function
