import newspaper
import json
from newspaper import fulltext
import requests

# According to https://en.wikipedia.org/wiki/Category:Lists_of_newspapers_by_country and some search work
# Recording websites for scraping
news_sites_by_country={
           'Afghanistan':['https://thekabultimes.gov.af/','http://outlookafghanistan.net/','https://www.afghanistantimes.af/'], 
           'India':['https://timesofindia.indiatimes.com/us','https://www.thehindu.com/','https://www.hindustantimes.com/'], 
           'Iran':['https://irandaily.ir/','https://ifpnews.com/','https://www.tehrantimes.com/'],
           'Kenya':['https://nation.africa/kenya','https://ksnmedia.com/','https://www.standardmedia.co.ke/','https://www.theeastafrican.co.ke/'],
           'Nigeria':['https://pmnewsnigeria.com/','https://www.naijanews.com/','https://independent.ng/'],
           'Sri Lanka':['https://sundaytimes.lk/','https://ceylontoday.lk/','https://island.lk/'],
           'Uganda':['https://www.newvision.co.ug/','https://www.monitor.co.ug/','https://www.bukedde.co.ug/',], 
           'Zimbabwe':['https://www.newsday.co.zw/','https://www.herald.co.zw/','https://www.newzimbabwe.com/','https://www.thestandard.co.zw/'],
           'Austria':['https://apnews.com/hub/austria','https://thelocalproject.com.au/','http://voiceofvienna.org/'], 
           'Australia':['https://www.heraldsun.com.au/','https://www.theaustralian.com.au/','https://www.theguardian.com/au','https://www.thesaturdaypaper.com.au/'],
           'Belgium':['https://www.brusselstimes.com/','https://www.thebulletin.be/','https://www.neweurope.eu/'], 
           'Finland':['https://www.dailyfinland.fi/','https://www.helsinkitimes.fi/','https://www.newsnow.co.uk/h/World+News/Europe/Northern+Europe/Finland'],
           'Netherlands':['https://nltimes.nl/','https://www.dutchnews.nl/'],
           'New Zealand':['https://www.nzherald.co.nz/','https://www.stuff.co.nz/dominion-post','https://www.stuff.co.nz/the-press'],
           'Norway':['https://norwaytoday.info/','https://www.thelocal.no/','https://www.newsinenglish.no/'], 
           'Sweden':['https://www.thelocal.se/','https://www.theguardian.com/world/sweden']}

# Recording urls scraped by program
news_url_by_country={
           'Afghanistan':[], 
           'India':[], 
           'Iran':[],
           'Kenya':[],
           'Nigeria':[],
           'Sri Lanka':[],
           'Uganda':[], 
           'Zimbabwe':[],
           'Austria':[], 
           'Australia':[],
           'Belgium':[], 
           'Finland':[],
           'Netherlands':[],
           'New Zealand':[],
           'Norway':[], 
           'Sweden':[]}


# news url extracter
for country,news_sites in news_sites_by_country.items():
    for news_site in news_sites:
        news_web = newspaper.build(news_site)
        for article in news_web.articles:
            news_url_by_country[country].append(article.url)

# write url to local
with open('./news_url.json','w') as f:
    json.dump(f)

# However, using newspaper library is not that good. The result is unbalanced. It might miss many urls due to different web designing format.
# e.g., running it for two days(once a day),the number of urls crawled by the library looks like:
# Afghanistan,0
# India,3294
# Iran,227
# Kenya,468
# Nigeria,310
# Sri Lanka,201
# Uganda,122
# Zimbabwe,576
# Austria,138
# Australia,617
# Belgium,443
# Finland,332
# Netherlands,182
# New Zealand,1153
# Norway,70
# Sweden,0

# What's more, there are some strange urls(perhaps advertisements)

# read url from local
with open('./news_url.json') as f:
    news_url_by_country = json.load(f)

# For news text storage
news_text_dict = {
           'Afghanistan':{}, 
           'India':{}, 
           'Iran':{},
           'Kenya':{},
           'Nigeria':{},
           'Sri Lanka':{},
           'Uganda':{}, 
           'Zimbabwe':{},
           'Austria':{}, 
           'Australia':{},
           'Belgium':{}, 
           'Finland':{},
           'Netherlands':{},
           'New Zealand':{},
           'Norway':{}, 
           'Sweden':{}
}

headers={
    'User-Agent':xxx
}

# Extract text from url
for country,url_list in news_url_by_country.items():
    for url in url_list:
        try:
            html = requests.get(url,headers=headers).text
            text = fulltext(html)
            news_text_dict[country][url]=text
        except:
            pass

with open('news_text.json','w') as f:
    json.dump(news_text_dict,f)