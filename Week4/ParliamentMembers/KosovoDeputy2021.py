from bs4 import BeautifulSoup
import requests

url = "https://kuvendikosoves.org/shq/deputetet/"
text = requests.get(url).text
soup = BeautifulSoup(text,'lxml') #or instead of lxml == html.parser
s = soup.find_all('h4', {'class':'name'})

for i in s:
    print(i)
