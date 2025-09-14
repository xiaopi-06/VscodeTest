import numpy as np
import pandas as pd

def calculate_quartiles(data):
    data.sort()
    n = len(data)
    q1 = data[int(n*0.25)]
    q2 = data[int(n*0.5)]
    q3 = data[int(n*0.75)]
    return q1, q2, q3

#定义数据
Data1 = [1, 2, 3, 3, 4, 4, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 9, 9, 10, 12, 12, 13, 15, 16, 18, 23, 55]
Data2 = [1, 2, 3, 4, 5, 6, 7, 8]
# df = pd.DataFrame(Data, columns=["values"])
#计算四分位数
# pdq3 = df["values"].quantile(0.75)
q1 = np.percentile(Data2, 25)
q2 = np.percentile(Data2, 50)
q3 = np.percentile(Data2, 75)
# q1, q2, q3 =calculate_quartiles(Data2)

print("第一分位数：", q1)
print("中位数：", q2)
print("第三分位数：", q3)
# print("pd第三四分位数", pdq3)