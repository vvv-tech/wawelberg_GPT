import requests
from bs4 import BeautifulSoup
from trafilatura.spider import focused_crawler
from wawelberg_sitemap import sitemap
from trafilatura import fetch_url, extract
import re

url_extract_pattern = "https?:\\/\\/(?:www\\.)?[-a-zA-Z0-9@:%._\\+~#=]{1,256}\\.[a-zA-Z0-9()]{1,6}\\b(?:[-a-zA-Z0-9()@:%_\\+.~#?&\\/=]*)"
links = re.findall(url_extract_pattern, sitemap)
print(links)

for link in links[:10]:
    if not 'wawelberg' in link:
        continue
    print(f"############## {link} ###############")
    downloaded = fetch_url(link)
    #print(extract(downloaded, include_links=True))
    #print('---------------')
    soup = BeautifulSoup(downloaded, "html.parser")
    regex = re.compile('.*descr* | .*tn-*')
    div_elems = soup.find_all("div", {"class" : regex})
    #print(div_elems)
    for div in div_elems:
        text = div.get_text()
        if len(text) > 10:
            print(text)
            print('-------------------------')
    print(f"############## {link} ###############\n\n\n")
