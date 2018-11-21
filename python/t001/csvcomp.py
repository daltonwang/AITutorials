#!/usr/bin/python
# -*- coding: UTF-8 -*-

import csv
import numpy as np

# 子函数 计算两个List的相关度


def corr(lista, listb, method):
    count = 0
    for i in lista:
        for j in listb:
            if i == j:
                count = count + 1
                
    a = len(lista)
    b = len(listb)
    total = a + b - count
    c1 = count / total
    c2 = count / b
    #print(count)
    #print(lista)
    #print(listb)
    #print("基准类%d样本,对比类%d样本,相同%d样本,总样本数目%d,相关性%d,相关性%d" %(a,b,count,total,c1,c2))
    if method == 1:
        return c1
    else:
        return c2

# 输入：input文件，output文件
# 处理：解析input文件和output文件中的各个类别的样本空间，计算各个样本空间的相似度，
# 方法1：（公共样本个数）/(样本总数)
# 方法2：（公共样本个数）/(output集合样本数)


# 1. get input file and output file
basedata = []
with open('input.csv', newline='') as csvfile:
    a = csv.reader(csvfile)
    for i in a:
        c = list(filter(None, i))
        d = list(map(int, c))
        basedata.append(d)
print("基准表中包括%d类" % len(basedata))


compdata = []
with open('result2018111801.csv', newline='') as csvfile:
    a = csv.reader(csvfile)
    for i in a:
        c = list(filter(None, i))
        d = list(map(int, c))
        compdata.append(d)
# print(compdata)
print("测试表中包括%d类" % len(compdata))

# 2. comp two set
len1 = len(basedata) #22类
len2 = len(compdata) #74类

corr1 = np.zeros((len1,len2))
corr2 = np.zeros((len1,len2))

j = 0
for seti in basedata:
    k = 0
    #print("-------------j=%d-------------" %j)
    for setj in compdata:
        #print("j=%d k=%d" %(j,k))
        corr1[j,k] = corr(seti, setj, 1)
        corr2[j,k] = corr(seti, setj, 2)
        #print("corr1=%d" %corr1[j,k])
        k = k+1
    j = j+1
out = open('corr1.csv','w', newline='')
csv_write = csv.writer(out)
for row in corr1:
	csv_write.writerow(row)
print("corr1 file output successed!")


out = open('corr2.csv','w', newline='')
csv_write = csv.writer(out)
for row in corr2:
	csv_write.writerow(row)
print("corr2 file output successed!")