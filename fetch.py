from bs4 import BeautifulSoup as bs
import requests
import json 

def fetcher(url):
    headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36(KHTML, like Gecklo) Chrome/56.0.2924.87 Safari/537.36',
    'referrer': 'https://google.com'}
    url = url
    response = requests.get(url, headers=headers)
    html = response.text.strip()
    return html

def proccessor(html):
    soup = bs(html,'html.parser')
    title = soup.title.text
    city = soup.h2.text.strip()
    city_class = soup.h2.text
    forecast = soup.find(class_="myforecast-current-lrg").text.strip()
    table = soup.table
    con = []
    # scraping a table in beautiful soup
    for i in soup.find_all('td'):
        con.append(i)
    barometer = con[5].text.strip()
    forecast_text = soup.find(class_="col-sm-10 forecast-text").text.strip()
    # print(soup.title.parent)  returns the parent elements
    # print(soup.title.parent.name) returns the name of the parent element
    return (title, city, forecast, barometer, forecast_text)

url = "https://forecast.weather.gov/MapClick.php?lat=40.6925&lon=-73.9904#.XAmGmRNKgWo"

data = fetcher(url)

print(proccessor(data))
