import requests
from bs4 import BeautifulSoup

#url = "https://thesmartlocal.com/read/december-2019-restaurants/"

'''
To get the name and address
'''
def getInfo(url):
    page = requests.get(url)

    #Create syntax tree
    soup = BeautifulSoup(page.text, 'html.parser')
    headers = soup.find_all("h3")
    for header in headers:
        addr = header.find_next("b", string=["Address:", "Address: "])
        if addr:
            print("{}\nAddress: {}".format(header.text, addr.find_next("span").text))



getInfo("https://thesmartlocal.com/read/december-2019-restaurants/")






    