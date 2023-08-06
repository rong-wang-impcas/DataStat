import sys
import numpy as np
import matplotlib.pyplot as plt

def display_data(data):
    plt.scatter(range(len(data)), data, marker='o', color='b')
    ##plt.plot(data)
    ##plt.xlabel("Index")
    plt.xlabel("Line number")
    plt.ylabel("Value")
    plt.title("Data Array")
    plt.grid(True)
    plt.show()

def read_data(file_path):
    data = []
    line_numbers = []
    with open(file_path, 'r') as file:
        for line_number, line in enumerate(file, 1):
            try:
                value = float(line.strip())
                data.append(value)
                line_numbers.append(line_number)
            except ValueError:
                print(f"Skipping line {line_number}: {line.strip()}. Not a valid numerical value.")

    return np.array(data), line_numbers

def find_outliers(data, z_threshold=3.0):
    mean = np.mean(data)
    std_dev = np.std(data)
    z_scores = np.abs((data - mean) / std_dev)
    outliers = data[z_scores > z_threshold]
    outlier_indices = np.where(z_scores > z_threshold)[0]

    return outliers, outlier_indices


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python datastat_display.py data.txt")
        sys.exit(1)

    file_path = sys.argv[1]
    data, line_numbers = read_data(file_path)

    if len(data) == 0:
        print("No valid numerical data found in the file.")
    else:
        outliers, outlier_indices = find_outliers(data)
        if len(outliers) > 0:
            print("\nOutliers found in the following lines:")
            for index in outlier_indices:
                print("In line number",index+1,":",data[index])
                ##print(f"Line {line_numbers[index]}: {outliers[index]}")
        else:
            print("No outliers found in the data.")


    display_data(data)
