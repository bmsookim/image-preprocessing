import cv2
import os
import sys
import file_function as ff
import config as cf

if __name__ == "__main__":
    if(len(sys.argv) < 2):
        print("\n[Error] : Set mode as your first arguement.\n")
        print("################## [ Options ] ###########################")
        print("# Mode 1 'print' : Print names of image data file")
        print("# Mode 2 'read'  : [original/aug] Read names data")
        print("# Mode 3 'resize': [target_size]  Resize & Orgnaize data")
        print("# Mode 4 'split' : Create a train-validation split of data")
        print("# Mode 5 'check' : Check the distribution of data")
        print("##########################################################")
        sys.exit(0)
    mode = sys.argv[1]

    ##############################################
    # @ Module 1 : Print names of image data file
    if (mode == 'print'):
        ff.print_all_imgs(cf.data_base)
    #############################################

    #############################################
    # @ Module 2 : Read all images
    if (mode == 'read'):
        if (len(sys.argv) < 3):
            print("[Error] : Please define the mode [original/aug] in the second arguement.")
        else:
            sub_mode = sys.argv[2]
            if(sub_mode == 'original'):
                ff.read_all_imgs(cf.data_base)
            elif(sub_mode == 'resized'):
                ff.read_all_imgs(cf.resize_dir)
            else:
                print("[Error] : Error in the second parameter: [original/aug]")
    #############################################

    #############################################
    # @ Module 3 : Resize and check images
    if (mode == 'resize'):
        if (len(sys.argv) < 3):
            print("[Error] : Please define size in the second arguement.")
        else:
            ff.check_and_mkdir(cf.resize_base)
            target_size = int(sys.argv[2])
            ff.resize_images(cf.data_base, cf.resize_dir, target_size)
    #############################################

    #############################################
    # @ Module 4 : Train-Validation split
    if (mode == 'split'):
        ff.check_and_mkdir(cf.split_base)
        split_dir = ff.create_train_val_split(cf.resize_dir, cf.split_dir)
        print("Train-Validation split directory = " + cf.split_dir)
    ############################################

    #############################################
    # @ Module 5 : Check the dataset
    if (mode == 'check'):
        ff.get_split_info(cf.split_dir)

    if (mode == 'count'):
        print("| " + cf.resize_dir.split("/")[-1] + " dataset : ")
        ff.count_each_class(cf.resize_dir)
    ############################################

    #############################################
    # @ Module 6 : Training data augmentation
    if (mode == 'aug'):
        ff.aug_train(cf.split_dir)
    #############################################

    #############################################
    # @ Module 7 : Retrieve Training data meanstd
    if (mode == 'meanstd'):
        mean = ff.train_mean(cf.split_dir)
        print(mean)
        std = ff.train_std(cf.split_dir, mean)
        print(std)
    #############################################
