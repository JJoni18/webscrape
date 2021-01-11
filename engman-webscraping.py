import requests
from bs4 import BeautifulSoup

#get the data
data = requets.get('https://umggamin.com/leaderboards')

#load data into bs4
soup = BeautifulSoup(data.text, 'html.parser')

leaderboard = soup.find('table', { 'id':'leaderboared-table'})
