import pandas

data = pandas.read_csv("weather_data.csv")
print(data["temp"])

#dataframe convertion
# data_dict = data.to_dict()
# print(data_dict)

#series convertion
# temp_list = data["temp"].to_list()
# print(data["temp"].mean())

# Get Data in row
print(data[data.day == "Monday"])
print(data[data.temp == data.temp.max()])

# #Create a dataframe from scratch
# data_dict = {
#     "students": ["Amy", "James","Angela"],
#     "scores":[76,56,65]
# }
#
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")
#print(data)

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count =len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
print(gray_squirrels_count)
print(red_squirrels_count)
print(black_squirrels_count)

data_dic = {
    "Fur color":["Gray","Cinnamon","Black"],
    "Count": [gray_squirrels_count,red_squirrels_count,black_squirrels_count]
}

df = pandas.DataFrame(data_dic)
df.to_csv("squirl_count_csv")
 