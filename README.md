# darknet_gui
simple standalone gui for YOLOv3 darknet. This specifically makes use of [darknet](https://github.com/AlexeyAB/darknet/) forked by AlexeyAB  for windows install. There are certainly better GUIs out there for YOLO and this is one is mainly for personal use.

## Install
- Install darknet YOLOv3 for windows ([darknet](https://github.com/AlexeyAB/darknet/))
- use `git clone` or direct download, then unzip to preferred directory.

## Usage
- run `py_main_gui.exe`
- Use `TEST GUI` with correct install directory of darknet x64 in the first field (ie. `C:/.../darknet/build/darknet/x64`)
  - This will just run the following commandline as a self test to check that the ui is working correctly:
  ```
  darknet.exe detector test cfg/coco.data yolov3.cfg yolov3.weights -ext_output dog.jpg
  ```
- Use the `Train` button to start dataset with correct directories to `*.data` `*.cfg` and `*.weights` (use `darknet53.conv.74` if new model). See file structure below. 
- The `create *.list` button assumes the following files structure:
```
.../x64/
       /<project workspace>/
                           /data/
                                /test/(store images and labels for testing)
                                /train/(store images and labels for training)
```
- `create *.list` looks into your project workspace, under the x64 darknet build, and looks through image file types (.png and .jpg) nested in data/train/ and data/test/ to make `train.list` and `test.list`. This keeps different projects in their seperate workspaces. 


## Change Log
### R01.003
- added `create *.list` function

### Known Issues with R01.003
- `Test` and `Test w/ Video` button needs to be worked on (maybe removed or changed)
