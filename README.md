image-preprocessing
====================================================================
Image pre-processing pipeline

Created at June 20, 2017

Korea University, Data-Mining & Information Systems Lab

Bumsoo Kim (meliketoy@gmail.com)

# Requirements
- python 2.7
- [OpenCV](http://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_gui/py_image_display/py_image_display.html)

# Input directory
The input directory should be in the given format:
```bash

[:folder]
    |-[:class 0]
        |-[:img 0]
        |-[:img 1]
        |-[:img 2]
        ...
    |-[:class 1]
    |-[:class 2]
    ...
        ...
            ...

```

# Modules

## 1. print
```bash
python main print
```
This module will print all the the file names of image related file formats(".jpg", ".png")

## 2. read
```bash
python main read
```
This module will read all the images and print out the spacial dimension of image related files.

## 3. resize
```bash
python main resize [:len]

# Example, to consist 256x256 images
python main resize 256
```
This module will save all the resized images into your given directory

## 4. split
```bash
python main split
```
This module will organize your input file directory into the following format.
You should manually set how much validation sets you want in your val class in val_num from [config.py](./config.py).

```bash
[:folder]
    |-train
        |-[:class 0]
            |-[:img 0]
            |-[:img 1]
            |-[:img 2]
            ...
        |-[:class 1]
        |-[:class 2]
        ...
            ...
                ...
    |-val
        |-[:class 0]
            |-[:img 0]
            |-[:img 1]
            |-[:img 2]
            ...
        |-[:class 1]
        |-[:class 2]
        ...
            ...
                ...

```

## 5. check
```bash
python main check
```
This will check how your data directory is consisted.
An example for the file directory after running module 4 (split) is as below.
```bash
$ python main check

| train set : 
    | false-positive   3345
    | true-positive    2547
| val set : 
    | false-positive    100
    | true-positive     100
```

## 6. augmentation
```bash
python main aug
```
This module will apply various image augmentations and enlarge your training set.
The input should be the splitted directory after running module 4 (split)
