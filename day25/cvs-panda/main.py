# data=[]
# with open("weather_data.csv","r") as f:
#     for line in f:
#         data.append(line)

# USING CSV
# import csv
# with open("weather_data.csv") as data_file:
#     data=csv.reader(data_file)
#     temperatures=[]
#     for row in data:
#         if row[1]=="temp":
#             pass
#         else:
#             temperatures.append(int(row[1]))
#
#     print(temperatures)

# USING PANDAS
import pandas

data = pandas.read_csv("weather_data.csv")  # creating data frame
# there is two primary data structure of pandas.Series (1-dimensional) and Frames (2-dimensional)
print(type(data))  # <class 'pandas.core.frame.DataFrame'> that means it is a pandas dataframe(2D)
print(type(data["temp"]))  # <class 'pandas.core.series.Series'>that is a pandas series(1D)

data_as_dict = data.to_dict()  # converting a dataframe to dictionary
data_as_list = data["temp"].to_list()  # converting a series to list
print(data_as_dict)
print(data_as_list)
print(sum(data_as_list) / len(data_as_list))  # finding average temp

avg = data["temp"].mean()  # mean() method finds the average of series

print(data["temp"].max())  # returns the max value of series

# Get Data In COLUMNS
print(data["condition"])  # this way you're treating the DataFrame as dictionary
print(data.condition)  # this way you're treating the DataFrame as object

# Get Data In ROWS
print(data[data.day == "Monday"])  # accessing the row which day is equal to monday

print(data[data.temp == data.temp.max()])  # print the row of the day has max temp

monday_row = data[data.day == "Monday"]
print(monday_row.condition)  # access to the data in specified row

# Create a DataFrame From Scratch
data_dict={
    "students":["Amy","James","Angela"],
    "scores":[76,56,65]
}
data2=pandas.DataFrame(data_dict) # creates a data frame
print(data2)
data2.to_csv("new_Data.csv")