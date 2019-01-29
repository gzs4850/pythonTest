#!/usr/bin/env python
#-*- coding:utf-8 -*-

import os
import random

def nsfile(s, size):

    # 生成文件
    for i in range(1, s + 1):
        filename = "data//" + str(i+400) + ".txt"
        ds = 0
        f = open(filename, 'w')
        while ds < size:
            f.write('test'+str(round(random.uniform(-1000, 1000), 2)))
            f.write("\n")
            ds = os.path.getsize(filename)


if __name__ == '__main__':
    nsfile(10, 1* 1024)