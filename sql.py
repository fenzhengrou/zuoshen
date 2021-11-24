# 只需要下载pandas包和sqlalchemy(pip install SQLAlchemy)
from sqlalchemy import create_engine
import pandas as pd

import random


# 生成一个虚拟数据库
engine = create_engine("sqlite:///:memory:")

#导入数据集heightWeight.csv
data1 = pd.read_csv('heightWeight.csv')
# 设置标签
data1.columns=["label",'col1','col2']

chars = ["a",'b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r',
         's','t','u','v','w','x','y','z',
         '-','=','_','+',',','.','?']

def generate_word(length=30):
    """
    随机生成长度为Length的单词，字符从chars里读取
    """
    word = []
    for i in range(len(chars)):
        idx = random.randint(1,len(chars)) - 1
        char = chars[idx]
        word.append(char)
    word = ''.join(word)
    return word


def generate_cols(length=210):
    """
    随机生成column里的内容
    """
    col = []
    for i in range(length):
        col.append(generate_word())
    return col

def generate_lbl(length=210):
    """
    随机生成标签（1或2）
    """
    labels = []
    for i in range(length):
        j = random.random()
        labels.append(1 if j < 0.5 else 2)
    return labels

length = 209
col1 = generate_lbl(length)
col2 = generate_cols(length)
col3 = generate_cols(length)
data2 = []

# 将三个columns的内容导入210*3的data2
for i in range(length):
    data2.append([col1[i],col2[i],col3[i]])
data2 = pd.DataFrame(data2, columns=["label",'col1','col2'])


# 将dataframe内容导入虚拟数据库 engine
data1.to_sql("data1", engine)
data2.to_sql("data2",engine)

# 连接数据库， 可以理解为with open(filename,'w') as f
# 其中conn为文件流名称
with engine.connect() as conn, conn.begin():
    # 将数据集通过 conn 导入数据库，
    data1 = pd.read_sql_table("data1", conn)
    data2 = pd.read_sql_table("data2", conn)
    # 传入SQL语句，得到结果
    a = pd.read_sql_query("SELECT data1.col1 as Data1Col1, data2.col1 as Data2Col1, sum(data1.col2) - sum(data2.col2) as MINUS "
                          "FROM data1 "
                          "left join data2 "
                          "where data1.label=data2.label "
                          "group by data1.col1, data2.col1", engine)
    print(a)
print(1)
