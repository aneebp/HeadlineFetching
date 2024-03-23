import requests #http request
from bs4 import BeautifulSoup #web scrapping




#extract new from HN using bs
def extract_news(url):
    cnt = ''
    cnt +=('<b> Header News Top Stories:</b>\n'+'<br>'+'-'*50+'<br>')
    response = requests.get(url)
    content = response.content
    soup = BeautifulSoup(content , 'html.parser')
    contents = soup.find_all('td',attrs={'class':'title'})
    for i in contents:
        print(i.text)
    




extract_news("https://news.ycombinator.com/")
