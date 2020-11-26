import plotly.figure_factory as ff
import random
import statistics 
import plotly.graph_objects as go

dice_result= []
for i in range(0,100):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    dice_result.append(dice1 + dice2)

#Calculating mean, median, mode and Standard Deviation(stdev)

mean = sum(dice_result) / len(dice_result)

median = statistics.median(dice_result)

mode = statistics.mode(dice_result)

standard_deviation = statistics.stdev(dice_result)

print("Mean of a data is {} ". format(mean))

print("Median of a data is {} ". format(median))

print("Mode of a data is {} ". format(mode))

print("Standard Deviation of a data is {} ". format(standard_deviation))

# finding the 1 standard deviation start & end values, 2 standard deviation, 3 standard deviation start & end values.

first_standard_deviation_start, first_standard_deviation_end = mean - standard_deviation, mean + standard_deviation

second_standard_deviation_start,second_standard_deviation_end =  mean - (2*standard_deviation), mean + (2*standard_deviation)
 
third_standard_deviation_start,third_standard_deviation_end  = mean - (3*standard_deviation), mean + (3*standard_deviation)

list_of_data_within_first_standard_deviation = [result for result in dice_result if result > first_standard_deviation_start and result < first_standard_deviation_end]

list_of_data_within_second_standard_deviation = [result for result in dice_result if result > second_standard_deviation_start and result < second_standard_deviation_end]

list_of_data_within_third_standard_deviation = [result for result in dice_result if result > third_standard_deviation_start and result < third_standard_deviation_end]

print("{}% of data lies within 1 standard deviation". format(len(list_of_data_within_first_standard_deviation)*100.0/len(dice_result)))

print("{}% of data lies within 2 standard deviation". format(len(list_of_data_within_second_standard_deviation)*100.0/len(dice_result)))

print("{}% of data lies within 3 standard deviation". format(len(list_of_data_within_third_standard_deviation)*100.0/len(dice_result)))


