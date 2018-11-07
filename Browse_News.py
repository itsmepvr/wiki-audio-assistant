 
# Program Name: Browse
#v_1.0
#Author : Venkata Ramana. P

from bs4 import BeautifulSoup
import requests
import urllib, urllib2
import wikipedia
from lxml import html
import requests

def browse_other(input):
    url='https://en.wikipedia.org/wiki/Allu_Arjun'
    content = urllib2.urlopen(url).read()
    soup = BeautifulSoup(content, "html.parser")
    final = []
    for row in soup.find_all('p'):
        final.append(row.text)
    print(final[0])
    return final[0]
    
        
def browse_wikipedia(input):
    output = wikipedia.summary(input)
    output1 = output.splitlines()
    print(output1[0])
    final = output1[0]
    return final

def browse_news():
    # Send request to get the web page
    response = requests.get('https://gadgets.ndtv.com/news')
    
    # Check if the request succeeded (response code 200)
    if (response.status_code == 200):
    
        # Parse the html from the webpage
        pagehtml = html.fromstring(response.text)
    
        # search for news headlines
        news = pagehtml.xpath('//a/span[@class="news_listing"]/text()')
        
    # Print each news item in a new line
    print("\n".join(news))
    final = "\n".join(news)
    return final
    
