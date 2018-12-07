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

def weather_proccessor(html):
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
    return (title, city, forecast, barometer, forecast_text)

def sec_proccessor(html):
    soup = bs(html, 'html.parser')
    table = soup.find('table',attrs={"class" : "tableFile2"})
    content = []
    for row in table.findAll("tr"):
        cells = row.findAll("td")
        cells = [ele.text.strip() for ele in cells]
    for row in table.findAll("a"):
        href = row.get("href")
        content.append(href)
    return content

def find_pageLink(content, target):
    """ take in a target page, search original links combined with uri to match target, if matched fetch page """
    target = target
    uri = "https://www.sec.gov"
    back_link = ""
    for i in content:
        if i in target:
            print("True")
            back_link = i
    url = "{}{}".format(uri,back_link)
    return url

# calls below
url = "http://www.sec.gov/cgi-bin/browse-edgar?CIK=grpn&Find=Search&owner=exclude&action=getcompany"
sec_data = fetcher(url)
content = sec_proccessor(sec_data)
url2 = find_pageLink(content,target="https://www.sec.gov/Archives/edgar/data/1490281/000149028118000124/0001490281-18-000124-index.htm")
foundSECData = fetcher(url2)
print(foundSECData)


