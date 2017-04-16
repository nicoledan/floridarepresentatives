from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import csv
html = urlopen("https://www.govtrack.us/congress/members/FL")
bsObj = BeautifulSoup(html, "html5lib")


reps = []
content = []

def getDetails(reps):
    global content
    for value in reps:
        bsObj = BeatifulSoup(html, "html.parser")
        names = bsObj.findAll("p", {"class":"moc"}).get_text,
        parties = bsObj.findAll("div", {"class":"info"}).get_text



def CSV(content):
    filename = "floridareps.csv"
    with open(filename, 'w') as output_file:
        fieldnames = [ 'names', 'parties' ]
        writer = csv.DictWriter(output_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(content)


getDetails(reps)
CSV(content)
