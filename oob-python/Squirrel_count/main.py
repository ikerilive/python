import pandas

#data = pandas.read_csv("weather_data.csv")

# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].to_list()
# average_temp = sum(temp_list) / len(temp_list)
# print(average_temp)

#maxi = data["temp"].max()
# print(maxi)

#Data in a row
# print(data[data.day == "Monday"])
# print(data[data.temp == maxi])

# monday = data[data.day == "Monday"]
# print((monday.temp * 9/5) + 32)

#import csv
# with open("./weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# with open("./weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     for row in data:
#         if row[1] != "temp":
#             temperature.append(int(row[1]))
#     print(temperature)

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20241117.csv")
grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
print(grey_squirrels_count)
print(cinnamon_squirrels_count)
print(black_squirrels_count)

data_dict = {
    "Fur Color": ["Grey", "Cinnamon", "Black"],
    "Count": [grey_squirrels_count, cinnamon_squirrels_count, black_squirrels_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")