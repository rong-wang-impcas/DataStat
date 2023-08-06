# DataStat

DataStat is for showing the statistics of a data sample and finding 
the outliers in the sample.

# Usage in the bash

**1. using datastat_display.py**

>python datastat_display.py data.txt

In datastat_display.py, the outliers are found by judging the z-score, 
with |z| > 3 defined as the outliers. 
The z-score of each data point is defined as, z = (x_i - mean) / sigma. 


**2. using datastat_boxplot.py**

>python datastat_boxplot.py data.txt

In datastat_boxplot.py, the outliers are found with the value lower 
than Q1 - 1.5*IQR or the value higher than Q3 + 1.5*IQR. 
IQR is defined as, IQR = Q3 - Q1. 
Q1 is the first quartile, and Q3 is the third quartile.
(The second quartile Q2 is the ordinary median.)


