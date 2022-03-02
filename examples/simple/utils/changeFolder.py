import sys
import random
import os
path = '../data/CASIA1/train'
j=0
files = os.listdir(path)
print(files)
# for i in os.listdir(path):
    # print(os.path)
    # os.rename(os)
    # path_file = os.path.join(path + '/'+i)
    # if os.path.isdir(path_file):  # 判断是不是一个文件夹
    #     file = os.listdir(path_file)
    #     n = 2
    #     for j in file[n:3]:  # 随机删除文件夹下末尾的文件
    #         os.remove(os.path.join(path_file) + '/'+j)
    #     # n = 4
    #     # for j in file[n:6]:  # 随机删除文件夹下末尾的文件
    #     #     os.remove(os.path.join(path_file) + '/'+j)