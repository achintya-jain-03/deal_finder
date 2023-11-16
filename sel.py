from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import undetected_chromedriver as webdriver
import pandas as pd
import re
#s=Service("C:/Users/ACHINTYA/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe")
#driver=webdriver.Chrome(service=s)
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--use_subprocess")

driver = webdriver.Chrome(options=chrome_options, version_main=119)


#driver.get("https://www.amazon.in/dp/B0744LQJ52/ref=sspa_dk_detail_1?psc=1&pd_rd_i=B0744LQJ52&pd_rd_w=BzEvp&content-id=amzn1.sym.2575ab02-73ff-40ca-8d3a-4fbe87c5a28d&pf_rd_p=2575ab02-73ff-40ca-8d3a-4fbe87c5a28d&pf_rd_r=4MJTWT7RNQXHYA67XH2X&pd_rd_wg=gdnIY&pd_rd_r=52c2b214-5eef-4dfb-b4cf-79d59db84760&s=shoes&sp_csd=d2lkZ2V0TmFtZT1zcF9kZXRhaWw")
#print(driver.find_element(By.XPATH,"""//*[@id="corePrice_feature_div"]/div/div/span[1]/span[2]/span[2]""").text)


#data = pd.read_csv("pokemon.csv")
df = pd.read_csv('file_name.csv')
df = df.drop_duplicates(subset=['Product'],keep='last')
i=int(input("Enter 1 to enter new products, else enter 2 to check status: "))

#Inserting products into the database
while(i==1):
    l = input("Enter link: ")
    tar_l = int(input("Enter target price: "))
    title=""
    try:
        driver.get(f"""{l}""")
    except:
        exit()
    if("amazon" in l):
        try:
            title=driver.find_element(By.XPATH,"""//*[@id="productTitle"]""").text
        except:
            title="-"
    elif("flipkart" in l):
        try:
            title=driver.find_element(By.XPATH,"""//*[@id="container"]/div/div[3]/div[1]/div[2]/div[2]/div/div[1]/h1/span[2]""").text
        except:
            title="-"

    df.loc[len(df)] = [title, l, tar_l]
    i=int(input("Enter 1 to continue, 2 to check status, anything else to stop: "))
df.to_csv('file_name.csv', index=False)


#check if element already exists in file
if(i==2):
    for index,row in df.iterrows():
        x=row["Link"]
        val=row["Price"]
        driver.get(f"""{x}""")
        time.sleep(3)
        if ("amazon" in x):
            price=driver.find_element(By.XPATH,"""//*[@id="corePrice_feature_div"]/div/div/span[1]/span[2]/span[2]""").text
            price = price.replace(",", "")
            val=int(df.loc[df['Link'] == x, 'Price'].values[0])

            if(int(price)==val):
                print(f"{row['Product']}  --TARGET REACHED !!")

        if("flipkart" in x):
            price=driver.find_element(By.XPATH,"""//*[@id="container"]/div/div[3]/div[1]/div[2]/div[2]/div/div[3]/div[1]/div/div[1]""").text
            price=price[1:]
            price= price.replace(",", "")
            val = int(df.loc[df['Link'] == x, 'Price'].values[0])
            if (int(price) == val):
                print(f"{row['Product']}   -- TARGET REACHED !!")

driver.close()