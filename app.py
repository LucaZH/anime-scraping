from bs4 import BeautifulSoup
import requests

class animescrap():
    def __init__(self):
        self.header = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:77.0) Gecko/20190101 Firefox/77.0"}
    def search(self,query):
        result,Title,Link,Synopsis,Img=([] for i in range(5))
        url = f"https://otakufr.co/toute-la-liste-affiches/?q={query}"
        req = requests.get(url,headers=self.header)
        soup = BeautifulSoup(req.content, 'lxml')
        divresult=soup.find('div',{"class":"col-md-8 order-1"})
        for img in divresult.find_all('img'):Img.append(img.get('src'))
        for textsyn in divresult.find_all('div',{'class':'except'}):Synopsis.append(textsyn.text)
        for name in divresult.find_all('a',{'class':'episode-name'}):
            Title.append(name.text.strip())
            Link.append(name.get('href'))
        if len(Link)==len(Synopsis):
            for i in range(len(Link)):
                result.append({
                "title":Title[i],
                "image":Img[i],
                "link":Link[i],
                "synopsis":Synopsis[i]
            })
        return result

    def getinfo(self,url):
        detail,resultinfo=([] for i in range(1))
        req = requests.get(url,headers=self.header)
        soup = BeautifulSoup(req.content, 'lxml')
        divresult=soup.find('div',{"class":"col-md-8 order-1"})
        synopsisdiv=divresult.find('div',{'class':'synop'})
        img=divresult.find('img').get('src')
        title= divresult.find('div',{'class':'title'}).text
        self.gettext(synopsisdiv,'p',detail)
        self.gettext(synopsisdiv,'li',detail)
        resultinfo.append({
            "title": title,
            "img":img,
            "detail":detail,
        })
        return resultinfo
    def gettext(self,parentbalise,childbalise,tab):
        for i in parentbalise.find_all(f'{childbalise}'):
            tab.append(i.text.replace('\t','').replace('\n','').replace('\xa0',''))
        return tab