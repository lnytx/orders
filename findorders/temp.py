'''
Created on 2017年3月30日

@author: ning.lin
'''
import os

import orders
import orders.settings
from multiprocessing.sharedctypes import template


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print("Base_dir",BASE_DIR)

print("1111",os.path.join(BASE_DIR, 'templates'))
#Base_dir D:\Program Files\Python_Workspace\orders
#D:\Program Files\Python_Workspace\orders\findorders\templates
#D:\Program Files\Python_Workspace\orders\findorders\templates
