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
Date: Feb 20 2019

"""

import os
import numpy as np
import shutil
import random
from glob import glob

all_zero_files = glob('*/0/*.png', recursive=True)
all_one_files = glob('*/1/*.png', recursive=True)

def make_directory(classname, val_split = 0.2):
"""
    # Arguments
        classname: Name of class -- either '0' or '1'.
        val_split: Optional argument -- percent to split
                   validation set. The default is 0.2. 
"""

    if classname == '0':
        filenames = all_zero_files
    else:
        filenames = all_one_files

    print('Building directory for class {}' .format(classname))

    for f in filenames:
        _, _, file =f.split('/')
        
        if np.random.rand(1) < val_split:
            shutil.move(f, 'data/val/' + classname + '/' + file)
        else:
            shutil.move(f, 'data/train/' + classname + '/' + file) 

make_directory('0')
make_directory('1')
