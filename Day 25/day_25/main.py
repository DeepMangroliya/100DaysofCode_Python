# import pandas as pd
#
# data = pd.read_csv("weather_data.csv")
# print(type(data))
# # print(data["temp"])
#
# data_dict = data.to_dict()
# print(data_dict)
# temp_list = data['temp'].to_list()
# print(temp_list)
#
# #average of temperature column
# # print(sum(temp_list)/len(temp_list))
# print(data['temp'].mean())
# print(data['temp'].max())
#
# print(data[data.temp == data.temp.max()])
#
# # get data in row
# monday = data[data.day == "Monday"]
# print(monday.condition)
# far = (monday.temp * 9/5) + 32
# print(far)
#
# # create dataframe from scratch
# data_dict = {
#     'students': ["Deep","Dep",'Dip'],
#     "scores": ["100","97","100"]
# }
# data = pd.DataFrame(data_dict)
# print(data)
# data.to_csv("new_data.csv")
# # import csv
#
# # with open("weather_data.csv", mode='r') as data_file:
# #     data = data_file.readlines()
# #     print(data)
# # # print(data)
#
# # with open("weather_data.csv", mode='r') as data_file:
# #     data = csv.reader(data_file)
# #     temperatures = []
# #     for row in data:
# #         if row[1]!='temp':
# #             temperatures.append(int(row[1]))
# #         # print(row)
# #     print(temperatures)

import pandas as pd

data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240714.csv")
gray_squirrels_count = len(data[data["Primary Fur Color"] == 'Gray'])
red_squirrels_count = len(data[data["Primary Fur Color"] == 'Cinnamon'])
black_squirrels_count = len(data[data["Primary Fur Color"] == 'Black'])

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrels_count, red_squirrels_count, black_squirrels_count]
}

df = pd.DataFrame(data_dict).to_csv("squirrel_count.csv")