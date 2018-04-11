############# Configuration file #############

# Name of dataset
# name = 'cells'
# name = 'HAPTIC_S'
# name = 'LH'
# name = 'NH'
# name = 'INBREAST_TRAIN'
name = 'Kaggle'
# name = 'GURO_TRAIN'
# name = 'GURO_ALL'
# name = 'INBREAST_ALL'
# name = 'MIX_TRAIN'
# name = 'TRANSFER'
# name = 'inbreast_patches_'
# name = 'guro_patches_test_'
# name = 'GURO80+INBREAST'
# name = 'INBREAST80+GURO'

# Base directory for data formats
data_base = '/mnt/datasets/' + name

# Base directory for augmented data formats
#resize_base = '/home/bumsoo/Data/resized/'
#split_base = '/home/bumsoo/Data/split/'
resize_base = '/home/bumsoo/Data/'
split_base = '/home/bumsoo/Data/'

# Directory for data formats
resize_dir = resize_base + name
split_dir = split_base + name

# Validation split
val_num = 100
val_ratio = 0.2
