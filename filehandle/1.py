#!/usr/bin/python3
# -*- conding:utf-8 -*-
__author__ = '170101'

import csv

filepath1 = "E:\\dev\\testData\\xzwl.csv"
filepath2 = "E:\\dev\\testData\\xzwl2.csv"

lists = []

with open(filepath1,'r') as f:
    reader = csv.reader(f)
    rows = [row for row in reader]

    for i in range(0,len(rows)):
        if rows[i][3] == '1':
            rows[i][3] = '01'
        elif rows[i][3] =='2':
            rows[i][3] = '02'
        lists.append([rows[i][0].strip(), rows[i][1].strip(), rows[i][2].strip(), rows[i][3].strip()])
    print(lists)

    # for list in lists:
    #     # print(list)
    #     write.writerow(list)
    # f2.close()


    with open(filepath2, 'w',newline='') as f:
        write = csv.writer(f)
        for list in lists:
            print(list)
            write.writerow(list)
        print("写入完毕！")





