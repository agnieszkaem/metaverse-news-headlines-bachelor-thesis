import csv
import web_scraper as ws

def save_to_csv(name,articles):
    header = ['newspaper','title', 'date','abstract','link']
    f = open(f'{name}.csv', 'w', encoding="utf-8-sig", newline='')
    writer = csv.writer(f,delimiter=";")
    writer.writerow(header)
    for a in articles:
        writer.writerow(a)
    f.close()


url1 = 'https://www.dailymail.co.uk/home/search.html?size=50&sel=site&searchPhrase=Metaverse&sort=recent&channel=reuters&channel=sciencetech&channel=news&channel=afp&channel=ap&channel=pa&channel=aap&channel=moneymarkets&channel=moneyinvesting&type=article&days=all&offset='
mail_online = ws.read_articles(name="Mail Online",
                            url_base=url1, 
                            start_page=0,
                            pages=13,
                            increment=50,
                            article='div',
                            article_class='sch-res-content',
                            el_tit='h3',
                            title_class='sch-res-title',
                            el_date='h4',
                            date_class='sch-res-info',
                            el_cont='p',
                            cont_class='sch-res-preview',
                            link_class= "")

                            
url2 = 'https://www.thetimes.co.uk/search?filter=all&q=metaverse&source=nav-desktop&p='
the_times = ws.read_articles(name="The Times",
                          url_base=url2,
                          start_page=1,
                          pages=31,
                          increment=1,
                          article="li",
                          article_class="Item ArticleList-item ArticleList-item--noMedia", 
                          el_tit="h2",
                          tit_class= "Item-headline Headline--s Headline--regular",
                          el_date="span",
                          date_class="Dateline Item-dateline",
                          el_cont="p",
                          cont_class="Item-dip Dip Dip--m",
                          link_class= "")


                          
url3 = "https://www.ft.com/search?q=metaverse&contentType=article&dateTo=2023-12-31&dateFrom=2021-01-01&sort=relevance&expandRefinements=true&page="
financial_times = ws.read_articles(
    name="Financial Times",
    url_base=url3,
    start_page=1,
    pages=25,
    increment=1,
    article="li",
    article_class="search-results__list-item",
    el_tit="div",
    tit_class= "o-teaser__heading",
    el_date= "time",
    date_class="o-teaser__timestamp-date",
    el_cont="a",
    cont_class="js-teaser-standfirst-link",
    link_class="js-teaser-heading-link")
 

url4 = 'https://www.bbc.co.uk/search?q=metaverse&d=HOMEPAGE_GNL&page='
bbc_uk= ws.read_articles(
              name= 'BBC', 
              url_base = url4,
              start_page=1,
              pages=20,
              increment=1,
              article= 'div',
              article_class='ssrcss-tq7xfh-PromoContent e1f5wbog8',
              el_tit= 'a',
              tit_class = 'ssrcss-rl2iw9-PromoLink e1f5wbog1', 
              el_date = 'span',
              date_class ='ssrcss-1if1g9v-MetadataText ecn1o5v1',
              el_cont='p',
              cont_class='ssrcss-1q0x1qg-Paragraph eq5iqo00',
              link_class='')


url5= 'https://www.forbes.com/simple-data/search/more/?q=metaverse&sh=1f445add279f&start='
forbes = ws.read_articles(name= 'Forbes', 
              url_base = url5,
              start_page=0,
              pages=50,
              increment=20,
              article= 'article',
              article_class='stream-item',
              el_tit= 'a',
              tit_class = 'stream-item__title', 
              el_date = 'div',
              date_class ='stream-item__date',
              el_cont='div',
              cont_class='stream-item__description',
              link_class='')










url6 = 'https://www.bloomberg.com/markets2/api/search?query=metaverse&sort=time:desc&page='
bloom= ws.get_articles_json(
    name='Bloomberg',
    start=1,
    end=120,
    url_link=url6,
    results='results',
    headline='headline',
    date='publishedAt',
    summary='summary',
    link='url',
    nxt_page= 1)



url7 = 'https://api.queryly.com/cnbc/json.aspx?queryly_key=31a35d40a9a64ab3&query=metaverse&batchsize=10&callback=&showfaceted=false&timezoneoffset=-60&facetedfields=formats&facetedkey=formats%7C&facetedvalue=!Press%20Release%7C&sort=date&additionalindexes=4cd6f71fbf22424d,937d600b0d0d4e23,3bfbe40caee7443e,626fdfcd96444f28&endindex='

cnbc =ws.get_articles_json(name="CNBC",
 start=0,
 end=880,
 url_link=url7,
 results='results',
 headline='cn:title',
 date='cn:lastPubDate',
 summary='description',
 link='url',
 nxt_page=10)


