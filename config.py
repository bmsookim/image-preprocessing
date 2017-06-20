############# Configuration file #############

# Base directory for data formats
data_base = '/mnt/datasets/GURO_FPTP'

# Base directory for augmented data formats
aug_base = '/home/bumsoo/Data/GURO_FPTP'

# model option
depth = 18
batch_size = 16
num_epochs = 25
lr_decay_epoch = 10
init_lr = 1e-3
feature_size = 100

# data_option
mean = [0.456, 0.456, 0456]
std = [0.224, 0.224, 0.224]
