import datetime


import requests


USERNAME = "abdulkerim"
TOKEN = "dwuiywjwu3yuy3283ru3r"
GRAPH_ID = "graph1"


pixel_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token":TOKEN,
    "username":USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes",
}

# response = requests.post(url=pixel_endpoint,json=user_params)
# print(response.text)

graph_endpoint = f"{pixel_endpoint}/{USERNAME}/graphs"

graph_config ={
    "id": GRAPH_ID,
    "name": "cycling graph",
    "unit":"km",
    "type":"float",
    "color":"ajisai"
}

headers = {
    "X-USER-TOKEN":TOKEN
}

# response = requests.post(url=graph_endpoint,json=graph_config,headers=headers)
# print(response.text)

pixel_creation_endpoint = f"{pixel_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.datetime.now()

pixel_data = {
    "date":today.strftime("%Y%m%d"),
    "quantity": input("how many killometers did you cycle today? ")
}
response = requests.post(url=pixel_creation_endpoint,json=pixel_data,headers=headers)
print(response.text)

update_endpoint = f"{pixel_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime("%Y%m%d")}"
new_pixel_data = {
    "quantity": "22"
}
# response = requests.put(url=update_endpoint,json=new_pixel_data,headers=headers)
# print(response.text)
delete_endpoint = f"{pixel_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime("%Y%m%d")}"
# response = requests.delete(url=delete_endpoint,headers=headers)
# print(response.text)

