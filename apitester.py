import requests
import os
import json

url = "https://fakesneakysnake.pythonanywhere.com/getHelp"



response = requests.post(url, json = {"content": "hi"})

print(response.content)

