import cv2
import os
import numpy as np
import random

def random_contrast(image, lower=0.2, upper=1.8, seed=None):
    contrast_factor = np.random.uniform(lower, upper)
    return (image-np.mean(image))*contrast_factor + np.mean(image)

def random_brightness(image, max_delta=63, seed=None):
    delta = np.random.randint(-max_delta, max_delta)
    return image-delta

def random_crop(image, dim):
    if len(image.shape):
        W, H, D = image.shape
        w, h, d = dim
    else:
        W, H = image.shape
        w, h = size

    left, top = np.random.randint(W-w+1), np.random.randint(H-h+1)
    return image[left:left+w, top:top+h]

# only for grayscale img
def random_rotation(image):
    deg = random.randrange(1, 360)
    (h,w) = image.shape[:2]
    center = (w/2, h/2)
    mean_val = [0.0, 0.0, 0.0]

    for channel in range(3):
        one_channel = image[:,:,channel]
        outer = np.append(one_channel[0,:-1], one_channel[-1,1:])
        tmp = np.append(one_channel[:-1,-1], one_channel[1:,0])
        outer = np.append(outer,tmp)
        outer = outer.flatten()
        mean_val[channel] = np.mean(outer[outer!=0])

    M = cv2.getRotationMatrix2D(center, deg, 1.0)
    rotated = cv2.warpAffine(image, M, (w,h), borderMode = cv2.BORDER_CONSTANT, borderValue=mean_val)

    return rotated
