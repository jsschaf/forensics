import requests
import sys
import re

temp = 86800
# 100000 -> 95000 -> 90000 -> 85000 -> 80000
#ANSWER: 86753
url = 'https://weratepups.xyz'
headers = {'User-Agent': str(temp)}
response = requests.get(url, headers=headers)
normal = response.content
temp -= 1

while True:
    headers = {'User-Agent' : str(temp)}
    response = requests.get(url, headers=headers)
    if response.content != normal:
        break
        print(temp)
    temp -= 1
    print(temp)