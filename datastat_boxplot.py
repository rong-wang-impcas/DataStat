import sys
import matplotlib.pyplot as plt
import numpy as np


def display_boxplot_with_outliers(data_array):
    # Create a figure and axis
    fig, ax = plt.subplots()
    
    # Plot the boxplot
    boxplot = ax.boxplot(data_array)
    
    # Set the title and labels
    ax.set_title('Boxplot with Outliers')
    ax.set_xlabel('Data')
    ax.set_ylabel('Values')
    
    # Get the outliers and their indices
    outliers = boxplot['fliers'][0].get_data()[1]
    outlier_indices = np.where(np.isin(data_array, outliers))[0]

    if len(outliers) > 0:
        print("\nOutliers found in the following lines:")
        for index in outlier_indices:
            print("In line number",index+1,":",data_array[index])
    else:
        print("No outliers found in the data.")

    # Highlight the outliers with red points
    #ax.scatter(outlier_indices + 1, outliers, color='red', marker='o', label='Outliers')
    xx = []
    for index in outlier_indices:
        xx.append(1)
    ax.scatter(xx, outliers, color='red', marker='o', label='Outliers')

    # Show the plot
    plt.legend()
    plt.show()
    
    return outliers, outlier_indices



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




if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python datastat_boxplot.py data.txt")
        sys.exit(1)

    file_path = sys.argv[1]
    data, line_numbers = read_data(file_path)

    if len(data) == 0:
        print("No valid numerical data found in the file.")
    else:
        # Display the boxplot and get outliers with their indices
        outliers, outlier_indices = display_boxplot_with_outliers(data)




  
