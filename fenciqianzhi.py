#!/usr/bin/python27
# -*- coding: utf-8 -*-
import struct
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
sys.path.append('../')
import xlrd
import jieba
import jieba.analyse
import string
import re

from optparse import OptionParser

r='[ 　  ]+'
#r = '[\s+\.\!\/_,$%^*(+\"\':()->]+|[+——！，。？、~@#￥%……&*（）：；‘’“”《》 　  ]+|[\n]+|[\r]+|[\000]+|[\t]+|[\v]+'

def is_chinese(uchar):
    """判断一个unicode是否是汉字"""
    num=0
    for i in uchar:
        if i>= u'\u4e00' and i <= u'\u9fa5':
            num = num +1
        else:
            num = num
    return num

def getnum(sen):
    count=1
    ml = re.sub(r.decode("utf8"), ''.decode("utf8"), sen)
    seg_list = list(jieba.cut(ml))
    if len(seg_list):
        word=seg_list[-1]
        if is_chinese(word)>1:
            pass
        else:
            while is_chinese(word) < 2:
                count= count +1
                if len(seg_list)>=count:
                    word = seg_list[-count] + word
                    if is_chinese(word) > 1:
                        break
                else:
                    break

    else:
        word=[]
    return word







data = xlrd.open_workbook('result.xls')
table = data.sheets()[0]
table.col_values(2)
nrows = table.nrows
f = open("outfenci.txt", "w")
print nrows
for i in range(nrows):
    cell_3 = table.cell(i, 2).value
    cell_5 = table.cell(i, 5).value.replace("[", "").replace("]", "")
    if ", " in cell_5:
        cell_5l = cell_5.split(", ")
        for j in set(cell_5l):
            cell_3l = cell_3.split(j)
            for m in cell_3l[:-1]:
                allname=getnum(m)
                f.write(str(allname)+'|')


    else:
        if cell_5:
            if cell_3.split(cell_5):
                cell_3l = cell_3.split(cell_5)
                for m in cell_3l[:-1]:
                    allname = getnum(m)
                    f.write(str(allname)+'|')
    print 'completed schedule: %.2f'%((i+1)*100.00/nrows)+'%'
f.close()
