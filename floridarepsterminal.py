from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
html = urlopen("https://www.govtrack.us/congress/members/FL")
bsObj = BeautifulSoup(html, "html5lib")


names = bsObj.findAll("p", {"class":"moc"})
parties = bsObj.findAll("div", {"class":"info"})

for name in names:
    print(name.get_text())

for party in parties:
    print(party.get_text())
