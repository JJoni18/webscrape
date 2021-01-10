import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup

my_url = 'https://www.newegg.com/p/pl?d=ddr3+server+RAM'

#opening up connection, grabbing the page
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

#html parsing
page_soup = BeautifulSoup(page_html, "html.parser")

#grabs each product
 containers = page_soup.findAll("div",{"class":"item-container"})

for container in containers:
    brand = container.div.div.a.img["title"]

    title_container = container.findAll("a", {"class":"item-title"})
    product_name = title_container[0].text
