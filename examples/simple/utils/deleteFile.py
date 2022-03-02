import sys
import random
import os
path = '../data/newData/test'
for i in os.listdir(path):
    path_file = os.path.join(path + '/'+i)
    if os.path.isdir(path_file):  # 判断是不是一个文件夹
        file = os.listdir(path_file)
        n = 0
        for j in file[n:8]:  # 随机删除文件夹下末尾的文件
            os.remove(os.path.join(path_file) + '/'+j)
        # n = 4
        # for j in file[n:6]:  # 随机删除文件夹下末尾的文件
        #     os.remove(os.path.join(path_file) + '/'+j)