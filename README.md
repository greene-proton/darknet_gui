# darknet_gui
simple standalone gui for YOLOv3 darknet. This specifically makes use of [darknet](https://github.com/AlexeyAB/darknet/) forked by AlexeyAB and specifcally meant for windows install. There are certainly better GUIs out there for YOLO and this is one is mainly for personal use.

## Install
- Install darknet YOLOv3 for windows ([darknet](https://github.com/AlexeyAB/darknet/))
- Simple use git clone or direct download and unzip to your preferred directory.
- run `py_main_gui.exe`
- Use `TEST GUI` with correct install directory of darknet x64 in the first field (ie. `C:/.../darknet/build/darknet/x64`)
- Use `Train` to train dataset with correct directories to `*.data` `*.cfg` and `*.weights` (use `darknet53.conv.74` if new model)
- `create *.list` assumes the following files structure:
```
.../x64/
       /<project workspace>/
                           /data/
                                /test/(store images and labels for testing)
                                /train/(store images and labels for training)
```

### R01.003
- added `create *.list` function
