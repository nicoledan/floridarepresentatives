from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import csv
import re
#html=urlopen("http://www.politifact.com/personalities/matt-gaetz/")
#bsObj = BeautifulSoup(html, "html5lib")

links = ["http://www.politifact.com/personalities/matt-gaetz/",
"http://www.politifact.com/personalities/ted-yoho/",
"http://www.politifact.com/personalities/ron-desantis/",
"http://www.politifact.com/personalities/bill-posey/",
"http://www.politifact.com/personalities/val-demings/",
"http://www.politifact.com/personalities/daniel-webster/",
"http://www.politifact.com/personalities/gus-bilirakis/",
"http://www.politifact.com/personalities/charlie-crist/",
"http://www.politifact.com/personalities/kathy-castor/",
"http://www.politifact.com/personalities/dennis-ross/",
"http://www.politifact.com/personalities/vern-buchanan/",
"http://www.politifact.com/personalities/alcee-hastings/",
"http://www.politifact.com/personalities/lois-frankel/",
"http://www.politifact.com/personalities/debbie-wasserman-schultz/",
"http://www.politifact.com/personalities/frederica-wilson/",
"http://www.politifact.com/personalities/mario-diaz-balart/",
"http://www.politifact.com/personalities/carlos-curbelo/",
"http://www.politifact.com/personalities/ileana-ros-lehtinen/"]

for link in links:
    html = urlopen(link)
    bsObj = BeautifulSoup(html, "html5lib")

#html = urlopen(LINKS)


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

def get_ruling_details(bsObj):
    repname = bsObj.find("div", {"class":"statement__source"}).get_text()
    rulings = bsObj.findAll("span", {"class":"chartlist__count"})
    row = []
    row.append(repname)
    # create regex expression to get only the number - save as exp
    exp = re.compile('^(\d+)')
    for ruling in rulings:
        # get the regex-matching string out of a ruling
        m = exp.match(ruling.get_text())
        # append ONE ruling to list named row - group() is a
        # Python regex thing
        # https://docs.python.org/3/howto/regex.html
        row.append(m.group())
    # after loop complete, write the ONE row
    c.writerow( row )

#get_names(bsObj)
get_ruling_details(bsObj)
csvfile.close()
