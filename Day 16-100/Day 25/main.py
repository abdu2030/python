import pandas

data = pandas.read_csv("weather_data.csv")
# print(data["temp"])

#dataframe convertion
# data_dict = data.to_dict()
# print(data_dict)

#series convertion
# temp_list = data["temp"].to_list()
# print(data["temp"].mean())

#Get Data in row
print(data[data.day == "Monday"])
print(data[data.temp == data.temp.max()])

#Create a dataframe from scratch
data_dict = {
    "students": ["Amy", "James","Angela"],
    "scores":[76,56,65]
}

data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")
#print(data)