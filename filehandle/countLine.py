#!/usr/bin/env python
#-*- coding:utf-8 -*-

def countLine(thefilepath):
    count = 0
    with open(thefilepath, 'rb') as thefile:
        while True:
            buffer = thefile.read(100*1024*1024)
            if not buffer:
                break
            count += str(buffer, encoding = "utf8").count('\n')
    print(count)
    thefile.close( )

if __name__ == '__main__':
    path = "20181221163105.txt"
    countLine(path)