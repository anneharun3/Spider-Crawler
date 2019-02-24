from bs4 import BeautifulSoup
import urllib.request
from urllib.parse import urlparse
import re
import requests
a = []
htmltext=urllib.request.urlopen('https://www.youtube.com/')
soup=BeautifulSoup(htmltext)
res=soup.findAll('a',href=True)
for tag in res:
     b1=urllib.parse.urlparse(tag['href']).hostname
     b2 = urllib.parse.urlparse(tag['href']).path
     if (b1 is not None) and (b2 is not None):
        b3=b1+b2
        print(b3)
        a.append(b3)
print('displaying the list')
print(a)
