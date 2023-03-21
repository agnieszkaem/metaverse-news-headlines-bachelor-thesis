
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin




def read_articles(name, url_base,start_page,pages,increment,article,article_class, el_tit,tit_class, el_date,date_class,el_cont,cont_class,link_class):
    page =start_page
    articles = []
    headers = {
        "User-Agent" : "Mozilla/5.0 (Windows NT 6.1; rv:45.0) Gecko/20100101 Firefox/45.0",
        }
    
    while True:
        url = f"{url_base}{page}"
        r = requests.get(url, headers= headers)
        path = urljoin(url, '.')[:-1]
        soup = BeautifulSoup(r.content.decode("utf-8-sig"), "html.parser")
        html_elements = soup.find_all(article, {"class": article_class})
        
        for el in html_elements:
            try:
                name = name
                title = el.find(el_tit,{"class":tit_class}).get_text(strip=True).lower()
                date = el.find(el_date,{"class": date_class}).get_text(strip=True)
                content = el.find(el_cont, {"class":cont_class}).get_text(strip=True).replace("\n"," ")
                content= content.lower()
                if link_class!="":
                    link = el.find('a',{"class":link_class}, href=True)['href']
                else:
                    link = el.find('a', href=True)['href']
                link = str(path)+link
                articles.append([name,title,date,content,link])
            
                
            except(AttributeError, KeyError) as e:
                    #Advertisement in article sector
                #print(" extracting not article - advertisement:", e)
                continue
        page+=increment
        if page>pages*increment:
            break

        

    return articles



def get_articles_json(name,start,end,url_link,results,headline,date,summary,link, nxt_page):
    articles = []
    headers = {
        "User-Agent" : "Mozilla/5.0 (Windows NT 6.1; rv:45.0) Gecko/20100101 Firefox/45.0",
        }
    
    for pg_index in range(start,end+1,nxt_page):

        url = f'{url_link}{pg_index}'
        try: 
            r = requests.get(url,headers = headers)
            data = r.json()
            d = data[results]

            for info in d:
                articles.append([name,info[headline],info[date],info[summary],info[link]])
        except(AttributeError, KeyError) as e:
            pass
           
    return articles
