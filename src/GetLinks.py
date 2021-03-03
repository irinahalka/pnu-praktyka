from GetArea import GetArea

class GetLinks(GetArea):
    def getLinks(self):
        content_area = GetArea().getContentArea()
        links = []
        for country_link in content_area:
            country_items = country_link.find("a").get("href")
            links.append(country_items)
        return links
        
