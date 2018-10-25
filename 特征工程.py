import pandas as pd
import numpy as np
#导入训练集数据
ot=pd.read_csv('operation_TRAIN.csv')
tt=pd.read_csv('transaction_TRAIN.csv')
tagt=pd.read_csv('tag_TRAIN.csv')
#表连接tt+tagt
data1=pd.merge(tt,tagt,how='right',on='UID')
#去重
data1.drop_duplicates('UID',inplace=True)
#表连接data1+ot
data2=pd.merge(data1,ot,how='left',on='UID')
#去重
data2.drop_duplicates('UID',inplace=True)
data=data2
#UID排序
data.sort_values('UID',inplace=True)
#将UID作为索引
data.set_index('UID',inplace=True)
