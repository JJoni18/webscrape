import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup

my_url = 'https://www.newegg.com/p/pl?d=ddr3+server+RAM'

#opening up connection, grabbing the page
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
