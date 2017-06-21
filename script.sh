#!/bin/bash

# print option
export print=true

# read option
export read=true
export read_opt='aug'

# resize option
export resize=true
export img_size=256

# split option
export split=true

# check option
export check=true

# aug option
export aug=true

# main function
if [ ${print} == true ]; then
    echo "Print function activated."
    python main.py print
fi

if [ ${resize} == true ]; then
    echo "Resize function activated."
    python main.py resize ${img_size}
fi

if [ ${read} == true ]; then
    echo "Read function activated."
    python main.py read ${read_opt}
fi

if [ ${split} == true ]; then
    echo "Train-Validation split activated."
    python main.py split
fi

if [ ${check} == true ]; then
    echo "Check function activated."
    python main.py check
fi

if [ ${aug} == true ]; then
    echo "Training set augmentation is activated."
    python main.py aug
fi
