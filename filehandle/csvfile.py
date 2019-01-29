#!/usr/bin/python3
# -*- conding:utf-8 -*-
__author__ = '170101'

import csv

filepath1 = "E:\\dev\\testData\\wuliaotest.csv"
filepath2 = "E:\\dev\\testData\\wuliaotest2.csv"

lists = []

with open(filepath1,'r') as f:
    reader = csv.reader(f)
    rows = [row for row in reader]

    for i in range(0,len(rows)):
        # print("顺序：%d" % i)
        if rows[i][0]:
            lists.append([rows[i][0].lstrip(),rows[i][1].lstrip()])

        elif not rows[i][0]:

            # print("开始合并。。。")
            # print(len(lists))
            lists[-1][1] = lists[-1][1]+','+rows[i][1].lstrip()

    print(lists)

    # for list in lists:
    #     # print(list)
    #     write.writerow(list)
    # f2.close()


    with open(filepath2, 'w') as f:
        write = csv.writer(f)
        for list in lists:
            print(list)
            write.writerow(list)
        print("写入完毕！")





