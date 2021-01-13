from math import exp,log,sqrt
import re
import sys #?
import glob
import os

# file_read=open('log/text.txt', 'r')
# for i in file_read:
#     print(i.strip())
# file_read.close()

# input_file='C:/Users/TAKESHI/Desktop/数据分析/log'
# #其中，target 参数用于指定一个变量，该语句会将 expression 指定的结果保存到该变量中。w
# # with as 语句中的代码块如果不想执行任何语句，可以直接使用 pass 语句代替。
# for j in glob.glob(os.path.join(input_file,'*.txt')):
#     with open(j,'r') as readfile:
#         for i in readfile:
#             print(i)

# letter=['a','b','a','b']
# max_len=len(letter)
# file_name='log/text.txt'
# file_writer=open(file_name,'w')
# for i in range(max_len):
#     if i<max_len:
#         file_writer.write(letter[i]+'\n')
#     else:
#         file_writer.write('continue'+'\n')
# file_writer.close()

# my_number=[1,2,3,4,5,6]
# max_len=len(my_number)
# file_input='log/text.txt'
# file_writer=open(file_input,'a')#追加模式
# for i in range(max_len):
#     if i<max_len-1:
#         file_writer.write(str(my_number[i])+',')
#     else:
#         file_writer.write(str(my_number[i])+'\n')
# file_writer.close()

# #1
# list1=[1,2,3]
# list2=[4,5,6]
# list3=[7,8,9]
# list5=[]
# for i in range(len(list1)):
#     a=list1[i]+list2[i]+list3[i]
#     print("list[%d]\n" %(i))
#     print(a)

list1=['1','2','3']
list2=['howare',1,"hi"]
dict1={}
for value in range(len(list1)):
    if list1[value] not in dict1:
        dict1[list1[value]]=list2[value]
for key,value in dict1.items():#返回字典对

    print(key,value)
