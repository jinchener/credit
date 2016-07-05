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

#r='[ 　  ]+'
r = '[\s+\[\]【】「\.\!\/_,$%^*(+\"\':()->]+|[+——！，。？、~@#￥%……&*（）：；‘’“”《》 　  ]+|[\n]+|[\r]+|[\000]+|[\t]+|[\v]+'

def is_chinese(uchar):
    #返回一个unicode中汉字的字数
    num=0
    for i in uchar:
        if i>= u'\u4e00' and i <= u'\u9fa5':
            num = num +1
        else:
            num = num
    return num

def getnum(sen):
    #返回sen最后的汉字长度大于1的汉字组合
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

def fenci(sen):
    #去除sen中的符号进行分词，返回两个词组合的list
    count=1
    ml = re.sub(r.decode("utf8"), ''.decode("utf8"), sen)
    seg_list = list(jieba.cut(ml))
    if (len(seg_list)-1):
        wordlist=[]
        for i in range(len(seg_list)-1):
            if i<(len(seg_list)-2):
                if is_chinese(seg_list[i]+seg_list[i+1])>2:
                    wordlist.append(seg_list[i]+seg_list[i+1])
                else:
                    wordlist.append(seg_list[i]+seg_list[i+1]+seg_list[i+2])
            else:
                wordlist.append(seg_list[i]+seg_list[i+1])

    elif len(seg_list):
        wordlist=seg_list
    else:
        wordlist=[]

    return wordlist







data = xlrd.open_workbook('credict-20160630.xlsx')
table = data.sheets()[0]
#table.col_values(4)
nrows = table.nrows
f = open("outfenci.txt", "w")
print nrows
for i in range(nrows):
    cell_4 = table.cell(i, 3).value
    wordll=fenci(cell_4)
    f.write(str('|'.join(wordll))+'\n')
    print 'completed schedule: %.2f'%((i+1)*100.00/nrows)+'%'
f.close()
