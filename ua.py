import requests;
import sys;
import re;


temp = 27870;
url = 'https://weratepups.xyz/'
headers = {'User-Agent': str(temp)}
response = requests.get(url, headers=headers)
normal = response.content;


while True:
    headers = {'User-Agent': str(temp)}
    response = requests.get(url, headers=headers)
    if response.content != normal:
        print("FOUND");
        print(temp);
        print(response.content);
        break;
    temp += 1;
    print(temp);
