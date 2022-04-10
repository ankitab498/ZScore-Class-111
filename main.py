import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random
import pandas as pd
import csv

df = pd.read_csv("z-test-master/studentMarks.csv")
data = df["Math_score"].tolist()

#plotting the graph
# fig = ff.create_distplot([data],["Math Scores"], show_hist= False)
# fig.show()

#calculating the mean and standard deviation of the population data
mean = statistics.mean(data)
std_deviation = statistics.stdev(data)

print("mean of popultion:- ",mean)
print("Standard deviation of popultion:- ",std_deviation)



##  code to find the mean of 100 data points 1000 times 
#function to get the mean of the given data samples
# pass the number of data points you want  as counter
def random_set_of_mean(counter):
    dataset = []
    for i in range(0, counter):
        random_index= random.randint(0,len(data)-1)
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean



# Pass the number of time you want the mean of the data points as a parameter in range function in for loop
mean_list = []
for i in range(0,1000):
    set_of_means= random_set_of_mean(100)
    mean_list.append(set_of_means)


## calculating mean and standard_deviation of the sampling distribution.
std_deviationS = statistics.stdev(mean_list)
meanS = statistics.mean(mean_list)

print("--------------------------------------------")
print("mean of sampling distribution:- ",meanS)
print("Standard deviation of sampling distribution:- ", std_deviationS)

# ----------------------------- mean of data1.csv (iPad) -------------------------------------

df1 = pd.read_csv("z-test-master/data1.csv")
data1 = df1["Math_score"].tolist()

meanOfData1 = statistics.mean(data1)

print("------------------------------------------------------")
print("mean of marks for the student who got iPad: ",meanOfData1)


# ----------------------------- mean of data2.csv (extra classes) -------------------------------------

df2 = pd.read_csv("z-test-master/data2.csv")
data2 = df2["Math_score"].tolist()

meanOfData2 = statistics.mean(data2)

print("-----------------------------------------------------------")
print("mean of marks for the student who got extra classes: ", meanOfData2)


# ----------------------------- mean of data3.csv (funsheets) -------------------------------------

df3 = pd.read_csv("z-test-master/data3.csv")
data3 = df3["Math_score"].tolist()

meanOfData3 = statistics.mean(data3)

print("-----------------------------------------------------------")
print("mean of marks for the student who got funsheets: ", meanOfData3)


# --------------------- calculating z- score ----------------------------

# zscore = (newSampleMean - samplingMeanOfPopulation) / stdDevOfSampleOutOfPopulation

zScore3 = (meanOfData3 - meanS)/std_deviationS

print("-----------------------------------------------------------")
print("Z Score is : " , zScore3)



zScore2 = (meanOfData2 - meanS)/std_deviationS

print("-----------------------------------------------------------")
print("Z Score is : " , zScore2)


zScore1 = (meanOfData1 - meanS)/std_deviationS

print("-----------------------------------------------------------")
print("Z Score is : " , zScore1)