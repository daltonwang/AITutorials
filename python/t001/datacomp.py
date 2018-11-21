#!/usr/bin/python
# -*- coding: UTF-8 -*-

import xlrd

'''一、打开文件'''
xl = xlrd.open_workbook("input.csv")
 
'''二、获取sheet'''
print ("表名：",xl.sheet_names())#获取sheet名称
print ("句柄：",xl.sheets())#获取sheet对象
print ("表数：",xl.nsheets) #获取sheet总数


'''三、获取sheet内的汇总数据'''
table1 = xl.sheet_by_index(0) #index 0
name = table1.name
clos = table1.ncols
sigtype = table1.nrows


sigtype = clos
for num in range(0,sigtype):  #
	data=table1.row_values(num)
	del data[0]
	data2=list(data)
	data2.sort()
	length = len(data2)
	zero = 0
	i = 0
	while data2[i] == 0 :
		i = i +1
	data3=data2[i:length]
	#print(data2)
	print(data3)


