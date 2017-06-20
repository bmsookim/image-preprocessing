import os
import cv2
import sys
import csv

# print all the name of images in the directory.
def print_all_imgs(in_dir):
    for subdir, dirs, files in os.walk(in_dir):
        for f in files:
            file_path = subdir + os.sep + f
            if (is_image(f)):
                print(file_path)

# check if the given file is an image format
def is_image(f):
    return f.endswith(".png") or f.endswith(".jpg")

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
            if (is_image(f)):
                img = cv2.imread(file_path)
                print('{:<100} {:>10}'.format(file_path, str(img.shape)))
                # print(file_path + ",img size = "+str(img.shape))

# resize the imgs from in_dir, and save with exact same hierarchy in the out_dir
def resize_images(in_dir, out_dir, target_size):
    check_and_mkdir(out_dir) # sanity check for the target output directory

    for subdir, dirs, files in os.walk(in_dir):
        for f in files:
            file_path = subdir + os.sep + f
            if (is_image(f)):
                img = cv2.imread(file_path)
                resized_img = cv2.resize(img, (target_size, target_size), interpolation = cv2.INTER_CUBIC)
                class_dir = out_dir + os.sep + file_path.split("/")[-2]
                check_and_mkdir(class_dir) # sanity check for the target class directory

                file_name = class_dir + os.sep + file_path.split("/")[-1]
                print(file_name)
                cv2.imwrite(file_name, resized_img)

# count the direct one-step sub directories (which will represent the class name)
def class_info(in_dir, mode):
    class_lst = []

    for subdir, dirs, files in os.walk(in_dir):
        class_lst = dirs # the 'dirs' variable after the first os.walk loop will return the list of classes
        break

    if(mode == "len"):
        return (len(class_lst))
    elif(mode == "list"):
        return (class_lst)

# count the containing images of each classes
def count_each_class(in_dir):
    class_lst, cnt_lst = class_info(in_dir, "list"), []

    for class_dir in class_lst:
        class_count = 0
        for subdir, dirs, files in os.walk(in_dir + os.sep + class_dir):
            for f in files:
                file_path = subdir + os.sep + f
                if (is_image(f)):
                    class_count += 1

        print("\t| {:<15} {:>5}".format(class_dir, class_count))
        cnt_lst.append(class_count)

    return cnt_lst

# return whether the current phase is 'train' or 'validation'
def return_phase(num, val_num):
    if (num < val_num):
        return "val" + os.sep
    else:
        return "train" + os.sep

def return_split_dir(in_dir):
    file_name = in_dir.split("/")[-1] # Get the name of the dataset
    current_dir = file_name
    parent_dir = os.path.abspath(os.path.join(in_dir, os.pardir))
    split_dir = parent_dir + os.sep + "_" + current_dir
    # If the original file name was 'imagenet', the train-val splitted dir will be '_imagenet'

    return split_dir

# create a train-val sub-organized directory from the original class directory
def create_train_val_split(in_dir):
    split_dir = return_split_dir(in_dir)

    print("Saving train-val splitted images into %s" %(split_dir))
    check_and_mkdir(split_dir)
    class_lst = class_info(in_dir, "list")

    for phase in ["train", "val"]:
        phase_dir = split_dir + os.sep + phase # The output directory will be "_[:file_dir]/[:phase]/[:class]"
        check_and_mkdir(phase_dir)

        for cls in class_lst:
            cls_dir = split_dir + os.sep + phase + os.sep + cls # Where to read the image from
            check_and_mkdir(cls_dir)

    val_num = 100 # temporary

    for subdir, dirs, files in os.walk(in_dir):
        cnt = 0
        for f in files:
            file_path = subdir + os.sep + f
            if(is_image(f)):
                img = cv2.imread(file_path)
                cv2.imwrite(split_dir + os.sep + return_phase(cnt, val_num) + subdir.split("/")[-1] + os.sep + f, img)
                cnt += 1

    return split_dir

# get train-val information
def get_split_info(in_dir):
    split_dir = return_split_dir(in_dir)

    for phase in ["train", "val"]:
        print("| %s set : " %phase)
        count_each_class(split_dir + os.sep + phase)

    return split_dir

# train data augmentation
def aug_train(aug_dir):
    split_dir = return_split_dir(aug_dir)
    train_dir = split_dir + os.sep + "train"

    for subdir, dirs, files in os.walk(train_dir):
        for f in files:
            file_path = subdir + os.sep + f
            if (is_image(f)):
                print(file_path)
