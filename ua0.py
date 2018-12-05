import requests;
import sys;
import re;



temp = 86740;
print(str(temp).zfill(5))

url = 'https://weratepups.xyz/'
headers = {'User-Agent': str(temp)}
response = requests.get(url, headers=headers)
normal = response.content;
temp += 1;


while True:
    print(str(temp).zfill(5))
    headers = {'User-Agent': str(temp).zfill(5)}
    response = requests.get(url, headers=headers)
    if response.content != normal:
        print("FOUND")
        print(temp);
        print(response.content);
        break;

    temp += 1;
