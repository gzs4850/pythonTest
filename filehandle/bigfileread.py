#!/usr/bin/env python
#-*- coding:utf-8 -*-

def bigtxt_read(filename):
    with open(filename, 'r', encoding='utf-8') as data:
        count =0
        while 1:
            count += 1
            line = data.readline()
            if 1000000 == count:
                print(line)
            if not line:
                break
        print(count)


if __name__ == '__main__':
    filename = '20181221163105.txt'
    bigtxt_read(filename)