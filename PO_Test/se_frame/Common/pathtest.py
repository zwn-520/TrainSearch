# coding=utf-8
import os

dir1 = os.path.realpath(__file__)
# dir2,dir3 = dir1.split()
dir2 = os.path.split(dir1)[0]

dir3 = os.path.split(os.path.realpath(__file__))[0].split('C')[0]
dir4 = os.path.split(os.path.realpath(__file__))[0].split('C')[1]
print(dir1)
print(dir2)
print(dir3)
print(dir4)