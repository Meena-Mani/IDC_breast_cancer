"""
This script arranges the IDC data into the Keras data directory structure,
namely:
   data/
       train/
            class 0
            class 1
       val/
            class 0
            class 1

Author: Meena Mani
Data: June 20 2018

"""

import os
import numpy as np
import shutil
from glob import glob
import random

all_zero_files = glob('*/0/*.png', recursive=True)
all_one_files = glob('*/1/*.png', recursive=True)

def make_directory(classname):
    
    if classname == '0':
        filenames = all_zero_files
    else:
        filenames = all_one_files

    for f in filenames:
        _, _, file =f.split('/')
        
        if np.random.rand(1) < 0.2:
            shutil.move(f, 'data/val/'+ classname + '/'+ file)
        else:
            shutil.move(f, 'data/train/' + classname +'/'+ file) 

make_directory('0')
make_directory('1')
