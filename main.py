import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import random
import re

user_agents = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 13_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15',
]

list_links={}
l=input("Enter link: ")
tar_l=int(input("Enter target price: "))
m=input("Enter link: ")
tar_m=int(input("Enter target price: "))
list_links[l]=tar_l
list_links[m]=tar_m
#print(list_links)

for x in list_links:

    #print(requests.get("""https://www.flipkart.com/puma-wish-max-sneakers-men/p/itmbbf3801a20950?pid=SHOGMYDFYZHKUGUM&lid=LSTSHOGMYDFYZHKUGUMCZQ7UO&marketplace=FLIPKART&q=slip%20on&sattr[]=size&pageUID=1696667404831""",headers=headers).status_code)
    user_agent = random.choice(user_agents)
    print(user_agent)
    headers = {'User-Agent': user_agent}
    r = requests.get(x,headers=headers)
    if(r.status_code!=200):
        print(f"Unable to connect -{x}, status code:",r.status_code)
        continue
    #print(r.status_code)
    soup=BeautifulSoup(r.text,"lxml")
    print(soup)
    #print(soup.find("span",class_="a-price a-text-price a-size-medium apexPriceToPay").get_text())
    if("amazon" in x):
        price=soup.find("span",{"class": "a-price-whole"}).text
        if(price>list_links[x]):
            print("Target reached")
        print(price)

    if("flipkart" in x):
        price=soup.find("div",{"class":"_30jeq3 _16Jk6d"}).string
    if("ajio" in x):
        #print(soup)
        first=soup.findAll('div', class_='prod-sp')
        print(first)


        #print(price)
    #price=int(re.findall(r'\d+', price))
    #print(price+10000)





