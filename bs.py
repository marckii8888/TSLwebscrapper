import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import re

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
            addr = header.find_next("span", string=["Address:", "Address: "])
            if addr:
                #Can change to write to REST framework when set up
                if addr.find_next("span").text[-1] == '\n':
                    addr.find_next("span").text = addr.find_next("span").text.translate({ord('\n'): None})

                regexp = re.compile(r'Opening hours|44|Telephone:')
                if regexp.search(addr.find_next("span").text):
                    print('Contains Opening hours')
                    continue
                else:
                    f.write("{}\nAddress: {}\n".format(re.sub(r'^.*?. ', '', header.text), addr.find_next("span").text))
        except:
            continue



class bot():
    def __init__(self):
        self.driver = webdriver.Chrome()
    
    def getData(self):
        self.driver.get("https://thesmartlocal.com/category/things-to-do/food-things-to-do/food-guides-food-things-to-do/")
        sleep(1)
        f = open('data.txt', 'a')
        page=1
        for i in range(10): 
            handle = self.driver.window_handles;           
            if len(handle)>1:
                print('New tab opened!')
                self.driver.switch_to_window(handle[1])
                '''
                check is it correct page opened or not (e.g. check page's title or url, etc.)
                ...
                close tab and get back
                '''
                self.driver.close()
                self.driver.switch_to_window(handle[0])
                print('New tab close!')

            for link in range(1,11):
                y = self.driver.find_element_by_xpath('//*[@id="wrapper"]/section/div/div/div[1]/div[2]/article[{}]/div/div[2]/header/h1/a'.format(link))
                url = y.get_attribute('href')
                getInfo(url,f)
            try:
                print('Finish writting info for page {}'.format(page))
                next_page = self.driver.find_element_by_xpath('/html/body/section/section/div/div/div[1]/div[3]/a[4]')
                next_page.click()
                page+=1
                sleep(3)
                continue
            except:
                print('Finish!')
                break
            
x = bot()
x.getData()
# Emma softsserve
