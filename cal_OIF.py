import pandas as pd
from itertools import combinations
import numpy as np

def calculate_OIF(num1,num2,filepath1,filepath2):
    '''
    计算OIF
    :param num1: 总波段数
    :param num2: 每组波段数
    :param filepath1: 标准差文件路径
    :param filepath2: 相关系数文件路径
    '''  
    # 波段数
    n = int(num1)

    # 读取n个波段的标准差
    csv_file = filepath1
    data1 = pd.read_csv(csv_file,header=None,sep=',')
    
    # 读取n个波段的相关系数矩阵
    csv_file = filepath2
    data2 = pd.read_csv(csv_file,header=None,sep='\t')

    # 前n列是n个波段的标准差
    std_devs = data1.iloc[:, :n].values

    # n乘n是相关系数矩阵
    correlation_matrix = data2.iloc[:n, :n].values

    # 计算OIF
    def cal(combination, std_devs, correlation_matrix):
        indexes = list(combination)
        S = 0
        R = 0
        for i in indexes:
            S += std_devs[i]
            for j in indexes:
                if i != j and i < j: 
                    R += np.abs(correlation_matrix[i][j])
        oif = S/R
        return oif

    # 获取所有三波段组合的OIF
    combinations_of_3 = list(combinations(range(n), int(num2)))
    oif_results = []

    for comb in combinations_of_3:
        oif = cal(comb, std_devs[0], correlation_matrix)  # 假设std_dev只有一行数据，使用std_devs[0]
        comb = list(comb)
        comb[0] += 1
        comb[1] += 1
        comb[2] += 1
        oif_results.append((comb, oif))

    # 按OIF大小排序
    oif_results.sort(key=lambda x: x[1], reverse=True)
    print(oif_results)

    # 输出到CSV文件
    result_df = pd.DataFrame(oif_results, columns=['Combination', 'OIF'])
    result_df['Combination'] = result_df['Combination'].apply(lambda x: ', '.join(map(str, x)))
    result_df.to_csv('output.csv', index=False)