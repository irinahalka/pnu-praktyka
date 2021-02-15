from urllib.request import urlopen
from bs4 import BeautifulSoup


html = urlopen("https://en.numista.com/catalogue/index.php?ct=coin")
soup = BeautifulSoup(html, "html.parser")

all_items = soup.findAll("ul", class_="liste_pays")
 
for item in all_items :
    countries = item.findAll("li")
    for country in countries:
        country_items = country.findAll("a")
        for country_item in country_items:
            print(country_item.get_text())
            print(country_item.get('href'))
                
