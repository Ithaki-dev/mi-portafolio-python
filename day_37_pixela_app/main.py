# This is a app for use pixela API
import requests
import datetime

USERNAME = "rquesada"
TOKEN = "asd2dqwed23dsd23sd23"
pixela_endpoint = "https://pixe.la/v1/users"

# Get the day in yyyyMMdd format
today = datetime.datetime.now()
today = today.strftime("%Y%m%d")

# This is a dictionary with the parameters that we need to send to the API
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
# This create the user
# response = requests.post(pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config_params = {
    "id": "d01",
    "name": "Drive",
    "unit": "kilometers",
    "type": "float",
    "color": "ajisai",
}

# Create a new graph
# response = requests.post(url=graph_endpoint, json=graph_config_params, headers={"X-USER-TOKEN": TOKEN})
# print(response.text)

# Add a new pixel
pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/d01"

pixel_data = {
    "date": "20250320",
    "quantity": "1.11",
}

# response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers={"X-USER-TOKEN": TOKEN})
# print(response.text)

# Update a pixel
update_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/d01/{today}"
update_pixel_data = {
    "quantity": "5.32",
    "date": today,
}

# response = requests.put(url=update_pixel_endpoint, json=update_pixel_data, headers={"X-USER-TOKEN": TOKEN})
# print(response.text)

# Delete a pixel
delete_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/d01/20250320"
response = requests.delete(url=delete_pixel_endpoint, headers={"X-USER-TOKEN": TOKEN})
print(response.text)