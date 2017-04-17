from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
html = urlopen("http://www.politifact.com/personalities/matt-gaetz/")
bsObj = BeautifulSoup(html, "html5lib")


rulings = bsObj.findAll("div", {"class":"peepDetailRuling"})

for ruling in rulings:
    print(ruling.get_text())
