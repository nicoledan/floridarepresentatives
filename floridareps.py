from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import csv
# open new file for writing
html = urlopen("https://www.govtrack.us/congress/members/FL")
bsObj = BeautifulSoup(html, "html.parser")


csvfile = open("floridareps.csv", 'w')
c = csv.writer(csvfile)
# write the header row for CSV file
c.writerow(['name', 'party'])

def get_member_details(bsObj):
    members = bsObj.findAll("div", {"class":"member"})
    for member in members:
        row = []
        name = member.find("p", {"class":"moc"}).get_text()
        party = member.find("div", {"class":"info"}).find("div").get_text()
        row.append( name )
        row.append( party )
        c.writerow( row )

get_member_details(bsObj)

# write your for-loop here - including c.writerow( row ) in the loop

csvfile.close()
