from urllib.request import urlopen
from bs4 import BeautifulSoup


def get_content_area():
    html = urlopen("https://en.numista.com/catalogue/index.php?ct=coin")
    soup = BeautifulSoup(html, "html.parser")
    all_items = soup.findAll("ul", class_="liste_pays")
    for item in all_items :
        content_area = item.findAll("li")
        return content_area


def get_countries(content_area):
    for country in content_area:
        country_items = country.findAll("a")
        for country_item in country_items:
            print(country_item.get_text())
            print(country_item.get('href'))
    
 

def parse():

    get_countries(get_content_area())
    

parse()
