#coding:utf-8
import struct
import sys
sys.path.append('../')
reload(sys)
sys.setdefaultencoding( "utf-8" )

the_list = []
word_lst = []
word_dict = {}
with open("outfenci.txt","r") as f1 ,open("cipin.txt",'w') as f2:
    for line in f1:
        word_lst.append(line.strip().split('|'))

    for item in word_lst:
        for item2 in item:
            if   item2 not in word_dict:
                word_dict[item2] = 1
            else :
                word_dict[item2] += 1

    word_dictll=sorted(word_dict.items(), key=lambda d: d[1], reverse = True)
    for i in word_dictll:
        if len(i[0])>3:
            f2.write(i[0]+' '+str(i[1]))
            print len(i[0])
            f2.write('\n')
    #for key in word_dict:
    #    f2.write(key+' '+str(word_dict[key])+'\n')
f1.close()
f2.close()