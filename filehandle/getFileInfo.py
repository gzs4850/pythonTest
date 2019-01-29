# -*- coding: UTF8 -*-

import time
import os

'''把时间戳转化为时间: 1479264792 to 2016-11-16 10:53:12'''
def TimeStampToTime(timestamp):
    timeStruct = time.localtime(timestamp)
    return time.strftime('%Y-%m-%d %H:%M:%S', timeStruct)

'''获取文件的大小,结果保留两位小数，单位为MB'''
def get_FileSize(filePath):
    fsize = os.path.getsize(filePath)
    fsize = fsize / float(1024 * 1024)
    return round(fsize, 2)

'''获取文件的访问时间'''
def get_FileAccessTime(filePath):
    t = os.path.getatime(filePath)
    return TimeStampToTime(t)

'''获取文件的创建时间'''
def get_FileCreateTime(filePath):
    t = os.path.getctime(filePath)
    return TimeStampToTime(t)

'''获取文件的修改时间'''
def get_FileModifyTime(filePath):
    t = os.path.getmtime(filePath)
    return TimeStampToTime(t)

if __name__ == '__main__':
    path = "20181221163105.txt"
    # path = unicode(path, 'utf8')
    print(get_FileCreateTime(path))
    print(get_FileModifyTime(path))
    print(get_FileAccessTime(path))
    print(get_FileSize(path))
