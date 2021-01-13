import csv
import sys
import pandas as pd
#2.1
# input_file='log/supplier_data.csv'
# output_file='log/supplier_data_output.csv.csv'
# #output_file
# with open(input_file,'r',newline='') as csv_in:
#     with open(output_file,'w',newline='') as csv_out:
#         file_reader=csv.reader(csv_in,delimiter=',')#分隔符
#         file_writer=csv.writer(csv_out,delimiter=',')
#         for row in file_reader:
#             print(row)
#             file_writer.writerow(row)

#2.2
# input_file='log/supplier_data.csv'
# output_file='log/supplier_data_output.csv'
# #output_file
# with open(input_file,'r',newline='') as input_csv:
#     with open(output_file, 'w', newline='') as output_csv:
#         file_reader=csv.reader(input_csv)
#         file_writer=csv.writer(output_csv)
#         header=next(file_reader)#换一行
#         file_writer.writerow(header)
#         for row in file_reader:
#             supplier=str(row[0]).strip()
#             cost=str(row[3]).strip('$').replace(',',' ')
#             if supplier=='Supplier Z' or float(cost)>600:
#                 print(row)
#                 file_writer.writerow(row)

#pandas
# input_file='log/supplier_data.csv'
# output_file='log/supplier_data_output.csv'
# data=pd.read_csv(input_file)
# data['Cost']=data['Cost'].str.strip('$').astype(float)
# data_meet=data.loc[(data['Supplier Name'].str.contains('Z')) | (data['Cost']>700),:]#(index,colum)
# data_meet.to_csv(output_file,index=False)

#2.2.2
# input_file='log/supplier_data.csv'
# output_file='log/supplier_data_output.csv'
# select_date=['1/20/14','1/30/14']
# with open(input_file,'r',newline='') as csv_in:
#     with open(output_file, 'w', newline='') as csv_out:
#         file_reader=csv.reader(csv_in)
#         file_writer=csv.writer(csv_out)
#         header=next(file_reader)
#
        # for row in file_reader:
        #     date=row[4]
        #     if date in select_date:
        #         file_writer.writerow(row)

# pandas
# input_file='log/supplier_data.csv'
# output_file='log/supplier_data_output.csv'
# select_date=['1/20/14','2/10/14']
# data_frame=pd.read_csv(input_file)
# data_meet=data_frame.loc[data_frame['Purchase Date'].isin(select_date),:]
# data_meet.to_csv(output_file,index=False)

#2.3.1
# input_file='log/supplier_data.csv'
# output_file='log/supplier_data_output.csv'
# select_colums=[0,3]
# with open(input_file,'r',newline='') as csv_in:
#     with open(output_file, 'w', newline='') as csv_out:
#         file_reader=csv.reader(csv_in)
#         file_writer=csv.writer(csv_out)
#         for row_list in file_reader:
#             row_output=[]
#             for index in select_colums:
#                 row_output.append(row_list[index])
#             file_writer.writerow(row_output)

# pandas
# input_file='log/supplier_data.csv'
# output_file='log/supplier_data_output.csv'
# data_frame=pd.read_csv(input_file)
# data_meet=data_frame.loc[0:],['Cost','Supplier']

# 2.4
# input_file='log/supplier_data.csv'
# output_file='log/supplier_data_output.csv'
# row_counter=0
# with open(input_file,'r',newline='') as csv_in:
#     with open(output_file, 'w', newline='') as csv_out:
#         file_reader=csv.reader(csv_in)
#         file_writer=csv.writer(csv_out)
#         for row in file_reader:
#             if row_counter>=3 and row_counter<=13:
#                 file_writer.writerow(row)
#             row_counter+=1
#
# pandas
input_file='log/supplier_data.csv'
output_file='log/supplier_data_output.csv'
data_frame=pd.read_csv(input_file,header=None)
data_frame=data_frame.drop([0,1,2,3])#loc选行，iloc选列
data_frame.columns=data_frame.iloc[0]#选取单独列重新建立列索引
data_frame=data_frame.reindex(data_frame.index.drop(4))#从第四开始
data_frame.to_csv(output_file,index='False')

# 2.5
# input_file='log/supplier_data.csv'
# output_file='log/supplier_data_output.csv'
# with open(input_file,'r',newline='') as csv_in:
#     with open(output_file, 'w', newline='') as csv_out:
#         file_reader=csv.reader(csv_in)
#         file_writer=csv.writer(csv_out)
#         header_list=['1','2','3','4','5']
        file_writer.writerow(header_list)
        header=next(file_reader)
        for row in file_reader:
            file_writer.writerow(row)

# pandas
input_file='log/supplier_data.csv'
output_file='log/supplier_data_output.csv'
header_list=['11','12','13','14','15']
data_frame=pd.read_csv(input_file,header=None,names=header_list)
data_frame=data_frame.drop([0,1,2,3,4,5,6])
data_frame.to_csv(output_file,index=False)