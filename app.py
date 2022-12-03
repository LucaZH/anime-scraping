from bs4 import BeautifulSoup
import requests

def search(query):
    result=[]
    Title=[]
    Link=[]
    Synopsis=[]
    url = f"https://otakufr.co/toute-la-liste-affiches/?q={query}"
    header = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:77.0) Gecko/20190101 Firefox/77.0"}
    req = requests.get(url,headers=header)
    soup = BeautifulSoup(req.content, 'lxml')
    divresult=soup.find('div',{"class":"col-md-8 order-1"})
    for name in divresult.find_all('a',{'class':'episode-name'}):
        Title.append(name.text.strip())
        Link.append(name.get('href'))
    for textsyn in divresult.find_all('div',{'class':'except'}):
        Synopsis.append(textsyn.text)
    if len(Link)==len(Synopsis):
        for i in range(len(Link)):
            result.append({
            "title":Title[i],
            "link":Link[i],
            "synopsis":Synopsis[i]
        })
    return result