import requests
from bs4 import BeautifulSoup
import pandas as pd

def extract(page):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'}
    url = f'https://www.indeed.com/jobs?q=linux%20system%20security%20administrator&l&vjk=d818e62b99905916={page}'
    r = requests.get(url, headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    return soup

def transform(soup):
    divs = soup.find_all('div', class_ = 'jobsearch-SerpJobCard')
    for item in divs:
        title = item.find('a').text.strip()
        company = item.find('span', class_ ='company').text.strip()
        try:
            salary = item.find('span', class_ = 'salaryText').text.strip()
        except:
            salary = ''
        summary = item.find('div', {'class' : 'summary'}).text.strip().replace('\n', '')


       #job dictionary
        job = {
            'titel': title,
            'company': company,
            'salary': salary,
            'summary': summary
        }
        joblist.append(job)
    return

joblist = []

for i in range(0,40,10):
    print(f'Getting page, {i}')
    c = extract(0)
    transform(c)

df = pd.DataFrame(joblist)
print(df.head())
df.to_csv('jobs.csv')
