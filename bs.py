import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep


'''
To get the name and address
'''
def getInfo(url, f):
    page = requests.get(url)

    #Create syntax tree
    soup = BeautifulSoup(page.text, 'html.parser')
    headers = soup.find_all("h3")
    for header in headers:
        try:
            addr = header.find_next("b", string=["Address:", "Address: "])
            if addr:
                f.write("{}\nAddress: {}".format(header.text, addr.find_next("span").text))
        except:
            continue



class bot():
    def __init__(self):
        self.driver = webdriver.Chrome()
    
    def getData(self):
        self.driver.get("https://thesmartlocal.com/category/things-to-do/food-things-to-do/food-guides-food-things-to-do/")
        sleep(1)
        f = open('data.txt', 'a')
        for link in range(1,11):
            y = self.driver.find_element_by_xpath('//*[@id="wrapper"]/section/div/div/div[1]/div[2]/article[{}]/div/div[2]/header/h1/a'.format(link))
            url = y.get_attribute('href')
            getInfo(url,f)


# f = open('data.txt', 'w')
# getInfo("https://thesmartlocal.com/read/cafe-food-delivery-singapore/", f)
# f.close()


# /html/body/section/section/div/div/div[1]/div[2]/article[1]/div/div[2]/header/h1/a

# /html/body/section/section/div/div/div[1]/div[2]/article[2]/div/div[2]/header/h1/a

# /html/body/section/section/div/div/div[1]/div[2]/article[10]/div/div[2]/header/h1/a




    