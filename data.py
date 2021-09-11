import pandas as pd 
import statistics
import csv

df = pd.read_csv("StudentsPerformance.csv")
preparation_list = df["test preparation course"].to_list()
math_list = df["math score"].to_list()
reading_list = df["reading score"].to_list()
writing_list = df["writing score"].to_list()


preparation_mean = statistics.mean(preparation_list)
math_mean = statistics.mean(math_list)
reading_mean = statistics.mean(reading_list)
writing_mean = statistics.mean(writing_list)

preparation_median = statistics.median(preparation_list)
math_median = statistics.median(math_list)
reading_median = statistics.median(reading_list)
writing_median = statistics.median(writing_list)

preparation_mode = statistics.mode(preparation_list)
math_mode = statistics.mode(math_list)
reading_mode = statistics.mode(reading_list)
writing_mode = statistics.mode(writing_list)

print("Mean, Median and Mode of preparation is {}, {} and {} respectively".format(preparation_mean, preparation_median, preparation_mode))
print("Mean, Median and Mode of math is {}, {} and {} respectively".format(math_mean, math_median, math_mode))
print("Mean, Median and Mode of reading is {}, {} and {} respectively".format(reading_mean, reading_median, reading_mode))
print("Mean, Median and Mode of writing is {}, {} and {} respectively".format(writing_mean, writing_median, writing_mode))

preparation_std_deviation = statistics.stdev(preparation_list)
math_std_deviation = statistics.stdev(math_list)
reading_std_deviation = statistics.stdev(reading_list)
writing_std_deviation = statistics.stdev(writing_list)

prep_first_stdev_start, prep_first_stdev_end = preparation_mean - preparation_std_deviation, preparation_mean + preparation_std_deviation
prep_second_stdev_start, prep_second_stdev_end = preparation_mean-(2*preparation_std_deviation), preparation_mean+(2*preparation_std_deviation)
prep_third_stdev_start, prep_third_stdev_end = preparation_mean-(3*preparation_std_deviation), preparation_mean+(3*preparation_std_deviation)

math_first_stdev_start, math_first_stdev_end = math_mean - math_std_deviation, math_mean + math_std_deviation
math_second_stdev_start, math_second_stdev_end = math_mean-(2*math_std_deviation), math_mean+(2*math_std_deviation)
math_third_stdev_start, math_third_stdev_end = math_mean-(3*math_std_deviation), math_mean+(3*math_std_deviation)

reading_first_stdev_start, reading_first_stdev_end = reading_mean - reading_std_deviation, reading_mean + reading_std_deviation
reading_second_stdev_start, reading_second_stdev_end = reading_mean-(2*reading_std_deviation), reading_mean+(2*reading_std_deviation)
reading_third_stdev_start, reading_third_stdev_end = reading_mean-(3*reading_std_deviation), reading_mean+(3*reading_std_deviation)

writing_first_stdev_start, writing_first_stdev_end = writing_mean - writing_std_deviation, writing_mean + writing_std_deviation
writing_second_stdev_start, writing_second_stdev_end = writing_mean-(2*writing_std_deviation), writing_mean+(2*writing_std_deviation)
writing_third_stdev_start, writing_third_stdev_end = writing_mean-(3*writing_std_deviation), writing_mean+(3*writing_std_deviation)

prep_list_of_data_within_1_stdev = [result for result in preparation_list if result > prep_first_stdev_start and result < prep_first_stdev_end]
prep_list_of_data_within_2_stdev = [result for result in preparation_list if result > prep_second_stdev_start and result < prep_second_stdev_end]
prep_list_of_data_within_3_stdev = [result for result in preparation_list if result > prep_third_stdev_start and result < prep_third_stdev_end]

math_list_of_data_within_1_stdev = [result for result in math_list if result > math_first_stdev_start and result < math_first_stdev_end]
math_list_of_data_within_2_stdev = [result for result in math_list if result > math_first_stdev_start and result < math_first_stdev_end]
math_list_of_data_within_3_stdev = [result for result in math_list if result > math_first_stdev_start and result < math_first_stdev_end]

reading_list_of_data_within_1_stdev = [result for result in reading_list if result > reading_first_stdev_start and result < reading_first_stdev_end]
reading_list_of_data_within_2_stdev = [result for result in reading_list if result > reading_first_stdev_start and result < reading_first_stdev_end]
reading_list_of_data_within_3_stdev = [result for result in reading_list if result > reading_first_stdev_start and result < reading_first_stdev_end]

writing_list_of_data_within_1_stdev = [result for result in writing_list if result > writing_first_stdev_start and result < writing_first_stdev_end]
writing_list_of_data_within_2_stdev = [result for result in writing_list if result > writing_first_stdev_start and result < writing_first_stdev_end]
writing_list_of_data_within_3_stdev = [result for result in writing_list if result > writing_first_stdev_start and result < writing_first_stdev_end]

print("{}% of data for prep lies within 1 standard deviation".format(len(prep_list_of_data_within_1_stdev)*100.0/len(preparation_list)))
print("{}% of data for prep lies within 2 standard deviations".format(len(prep_list_of_data_within_2_stdev)*100.0/len(preparation_list)))
print("{}% of data for prep lies within 3 standard deviations".format(len(prep_list_of_data_within_3_stdev)*100.0/len(preparation_list)))

print("{}% of data for math lies within 1 standard deviation".format(len(math_list_of_data_within_1_stdev)*100.0/len(math_list)))
print("{}% of data for math lies within 2 standard deviations".format(len(math_list_of_data_within_2_stdev)*100.0/len(math_list)))
print("{}% of data for math lies within 3 standard deviations".format(len(math_list_of_data_within_3_stdev)*100.0/len(math_list)))

print("{}% of data for reading lies within 1 standard deviation".format(len(reading_list_of_data_within_1_stdev)*100.0/len(reading_list)))
print("{}% of data for reading lies within 2 standard deviations".format(len(reading_list_of_data_within_2_stdev)*100.0/len(reading_list)))
print("{}% of data for reading lies within 3 standard deviations".format(len(reading_list_of_data_within_3_stdev)*100.0/len(reading_list)))

print("{}% of data for writing lies within 1 standard deviation".format(len(writing_list_of_data_within_1_stdev)*100.0/len(writing_list)))
print("{}% of data for writing lies within 2 standard deviations".format(len(writing_list_of_data_within_2_stdev)*100.0/len(writing_list)))
print("{}% of data for writing lies within 3 standard deviations".format(len(writing_list_of_data_within_3_stdev)*100.0/len(writing_list)))