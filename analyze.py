import pandas as pd  
import numpy as np  

import sys




def find_outliers(data, z_threshold=3.0):
    mean = np.mean(data)
    std_dev = np.std(data)
    print("     Mean:",mean)
    print("     Std:",std_dev)
    print("     Cv: %.2f%%"%(100*std_dev/mean))
    z_scores = np.abs((data - mean) / std_dev)
    outliers = data[z_scores > z_threshold]
    outlier_indices = np.where(z_scores > z_threshold)[0]

    return outliers, outlier_indices




def analyze_xlsx_file(filename):
    # 读取Excel文件  
    df = pd.read_excel(filename, engine='openpyxl')  
    # 计算每列的平均值和标准偏差  
    for column in df.columns:
        print(" ",column+": ")
        # 去掉非法数值
        data_clean = df[column].dropna()
        if len(data_clean) < 3:
            print("     Too few data for",data_clean.name)
            print()
        else:
            find_outliers(data_clean, z_threshold=3.0)
            #print(type(df[column]))
            #print(df[column])
            print()





if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python analyze.py data.xlsx")
        sys.exit(1)

    file_path = sys.argv[1]
    analyze_xlsx_file(file_path)


