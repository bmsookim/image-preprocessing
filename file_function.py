import os
import cv2
import sys
import csv

# print all the name of images in the directory.
def print_all_imgs(in_dir):
    for subdir, dirs, files in os.walk(in_dir):
        for f in files:
            file_path = subdir + os.sep + f
            if (f.endswith(".png") or f.endswith(".jpg")):
                print(file_path)

# check if dir exists. If not, mkdir.
def check_and_mkdir(in_dir):
    if not os.path.exists(in_dir):
        print("Creating "+in_dir+"...")
        os.makedirs(in_dir)

# read and print all the image sizes of the dir.
def read_all_imgs(in_dir):
    for subdir, dirs, files in os.walk(in_dir):
        for f in files:
            file_path = subdir + os.sep + f
            if (f.endswith(".png") or f.endswith(".jpg")):
                img = cv2.imread(file_path)
                print('{:<100} {:>10}'.format(file_path, str(img.shape)))
                # print(file_path + ",img size = "+str(img.shape))

# resize the imgs from in_dir, and save with exact same hierarchy in the out_dir
def resize_images(in_dir, out_dir, target_size):
    check_and_mkdir(out_dir) # sanity check for the target output directory

    for subdir, dirs, files in os.walk(in_dir):
        for f in files:
            file_path = subdir + os.sep + f
            if (f.edswith(".png") or f.endswith(".jpg")):
                img = cv2.imread(file_path)
                resized_img = cv2.resize(img, (target_size, target_size), interpolation = cv2.INTER_CUBIC)
                class_dir = out_dir + os.sep + file_path.split("/")[-2]
                check_and_mkdir(class_dir) # sanity check for the target class directory

                file_name = class_dir + os.sep + file_path.split("/")[-1]
                print(file_name)
                cv2.imwrite(file_name, resize_img)
