import pandas

# data = pandas.read_csv("weather_data.csv")
# print(data["temp"])

#dataframe convertion
# data_dict = data.to_dict()
# print(data_dict)

#series convertion
# temp_list = data["temp"].to_list()
# print(data["temp"].mean())

#Get Data in row
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])
#
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
graySquirrels = data[data["Primary Fur Color"] == "Gray"]
 