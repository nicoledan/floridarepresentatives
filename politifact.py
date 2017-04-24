from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import csv
html = urlopen("http://www.politifact.com/personalities/matt-gaetz/")
bsObj = BeautifulSoup(html, "html5lib")

csvfile = open("politifact.csv", 'w')
c = csv.writer(csvfile)
# write the header row for CSV file
c.writerow(['representative', 'true', 'mostly true', 'half true', 'mostly false', 'false', 'pants on fire'])

def get_names (bsObj):
    names = bsObj.find("div", {"class":"statement__source"})
    for name in names:
        row = []
        representative = name.find("div", {"class":"statement__source"}).get_text()
        row.append( representative )
        c.writerow( row )

def get_ruling_details (bsObj):
    rulings = bsObj.findAll("li", {"class":"chartlist__item"})
    for ruling in rulings:
        row = []
        true_statement = ruling.find("span", {"class":"chartlist_count"}).get_text() [1::6]
        mostly_true = ruling.find("span", {"class":"chartlist_count"}).get_text() [2::6]
        half_true = ruling.find("span", {"class":"chartlist_count"}).get_text() [3::6]
        mostly_false = ruling.find("span", {"class":"chartlist_count"}).get_text() [4::6]
        false_statement = ruling.find("span", {"class":"chartlist_count"}).get_text() [5::6]
        pants_on_fire = ruling.find("span", {"class":"chartlist_count"}).get_text() [6::6]
        c.writerow( row )

get_names(bsObj)
get_ruling_details(bsObj)
