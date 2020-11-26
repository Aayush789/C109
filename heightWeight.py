import csv
import pandas as pd 
import statistics 

df = pd.read_csv("height-weight.csv")

height_list = df["Height(Inches)"].to_list()

height_mean = statistics.mean(height_list)

height_median = statistics.median(height_list)

height_mode = statistics.mode(height_list)

height_standard_deviation = statistics.stdev(height_list)

print("Mean of a data is {} ". format(height_mean))

print("Median of a data is {} ". format(height_median))

print("Mode of a data is {} ". format(height_mode))

print("Standard Deviation of a data is {} ". format(height_standard_deviation))

# finding the 1 standard deviation start & end values, 2 standard deviation, 3 standard deviation start & end values.

height_first_standard_deviation_start, height_first_standard_deviation_end = height_mean - height_standard_deviation, height_mean + height_standard_deviation

height_second_standard_deviation_start, height_second_standard_deviation_end =  height_mean - (2*height_standard_deviation), height_mean + (2*height_standard_deviation)
 
height_third_standard_deviation_start, height_third_standard_deviation_end  = height_mean - (3*height_standard_deviation), height_mean + (3*height_standard_deviation)

height_list_of_data_within_first_standard_deviation = [result for result in height_list if result > height_first_standard_deviation_start and result < height_first_standard_deviation_end]

height_list_of_data_within_second_standard_deviation = [result for result in height_list if result > height_second_standard_deviation_start and result < height_second_standard_deviation_end]

height_list_of_data_within_third_standard_deviation = [result for result in height_list if result > height_third_standard_deviation_start and result < height_third_standard_deviation_end]

print("{}% of data lies within 1 standard deviation". format(len(height_list_of_data_within_first_standard_deviation)*100.0/len(height_list)))

print("{}% of data lies within 2 standard deviation". format(len(height_list_of_data_within_second_standard_deviation)*100.0/len(height_list)))

print("{}% of data lies within 3 standard deviation". format(len(height_list_of_data_within_third_standard_deviation)*100.0/len(height_list)))

