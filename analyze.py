import pandas as pd  
import numpy as np  
import matplotlib.pyplot as plt
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
    if len(outliers) > 0:
        data_without_outliers = data[z_scores <= z_threshold]
        mean = np.mean(data_without_outliers)
        std_dev = np.std(data_without_outliers)
        print()
        print("     Mean after deleting outliers:",mean)
        print("     Std after deleting outliers:",std_dev)
        print("     Cv after deleting outliers: %.2f%%"%(100*std_dev/mean))

    return outliers, outlier_indices
def find_outliers_noprint(data, z_threshold=3.0):
    mean = np.mean(data)
    std_dev = np.std(data)
    z_scores = np.abs((data - mean) / std_dev)
    outliers = data[z_scores > z_threshold]
    outlier_indices = np.where(z_scores > z_threshold)[0]
    return outliers, outlier_indices




def analyze_xlsx_file(filename):
    # 读取Excel文件  
    df = pd.read_excel(filename, engine='openpyxl')  
    print()
    # 计算每列的平均值和标准偏差  
    for column in df.columns:
        print(" ",column+": ")
        # 去掉非法数值
        data_clean = df[column].dropna()
        if len(data_clean) < 3:
            print("     Too few data for",data_clean.name)
            print()
        else:
            outliers, indices = find_outliers(data_clean, z_threshold=3.0)
            if len(indices) > 0:
                print()
            for index in indices:
                print("     ***In line number %d:"%(index+2),data_clean[index],"is abnormal!!!")
            if len(indices) > 0:
                print()
            #print(type(df[column]))
            #print(df[column])
            print()








def display_xlsx_file(filename):
    # 读取Excel文件  
    df = pd.read_excel(filename, engine='openpyxl')  
    # 创建一个画布  
    nplots = len(df.columns)
    if nplots == 1:
        # 循环遍历每列数据并绘制散点图  
        for i, column in enumerate(df.columns):  
            # 去掉非法数值
            data_clean = df[column].dropna()
            if len(data_clean) >= 1:
                plt.scatter(range(2,len(data_clean)+2), data_clean, marker='o', color='b')  
                plt.title(column)  
                plt.xlabel('Line number')
                plt.ylabel('Value') 
            outliers, indices = find_outliers_noprint(data_clean, z_threshold=3.0)
            if len(indices) >= 1:
                indices = indices + 2
                plt.scatter(indices, outliers, marker='o', color='r')
    elif nplots <= 10:
        fig, axs = plt.subplots(ncols=nplots, figsize=(13, 4.5)) 
        # 循环遍历每列数据并绘制散点图  
        for i, column in enumerate(df.columns):  
            # 去掉非法数值
            data_clean = df[column].dropna()
            if len(data_clean) >= 1:
                ax = axs[i]
                ax.scatter(range(2,len(data_clean)+2), data_clean, marker='o', color='b')
                ax.set_title(column)  
                ax.set_xlabel('Line number')
                ax.set_ylabel('Value')  
            outliers, indices = find_outliers_noprint(data_clean, z_threshold=3.0)
            if len(indices) >= 1:
                indices = indices + 2
                ax.scatter(indices, outliers, marker='o', color='r')
        # 调整子图间距  
        plt.tight_layout(pad=3) 
    else:
        print("  !!! Too many data to display! No figures generated!\n")
    # 展示画布  
    plt.show()





if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python analyze.py data.xlsx")
        sys.exit(1)

    file_path = sys.argv[1]
    analyze_xlsx_file(file_path)
    display_xlsx_file(file_path)


