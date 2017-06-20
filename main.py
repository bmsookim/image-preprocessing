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
            elif(sub_mode == 'aug'):
                ff.read_all_imgs(cf.aug_base)
            else:
                print("[Error] : Error in the second parameter: [original/aug]")
    #############################################

    #############################################
    # @ Module 3 : Resize and check images
    if (mode == 'resize'):
        if (len(sys.argv) < 3):
            print("[Error] : Please define size in the second arguement.")
        else:
            target_size = int(sys.argv[2])
            ff.resize_images(cf.data_base, cf.aug_base, target_size)
    #############################################

    #############################################
    # @ Module 4 : Train-Validation split
    if (mode == 'split'):
        print(cf.aug_base)
        split_dir = ff.create_train_val_split(cf.aug_base)
        print("Train-Validation split directory = " + cf.aug_base)
    ############################################

    #############################################
    # @ Module 5 : Check the dataset
    if (mode == 'check'):
        ff.get_split_info(cf.aug_base)
    ############################################

    ############################################
    # @ Module 6 : Obtain Global meanstd
    if (mode == 'meanstd'):
        mean, std = ff.train_meanstd(cf.aug_base)
        print(mean ,std)
    ############################################
