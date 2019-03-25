import requests
from bs4 import BeautifulSoup

for link in BeautifulSoup(requests.get('https://www.google.com/search?q=online+shopping+kenya&oq=online+shopping+kenya&aqs=chrome..69i57j69i60l2j0l3.7826j0j9&sourceid=chrome&ie=UTF-8').content).find_all("div", {"class":"r"}):
    if "http" in link.get("href"):
        print ("<a href='%s'>%s</a>" %(link.get("href"), link.text))
