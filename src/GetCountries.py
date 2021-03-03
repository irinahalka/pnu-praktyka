from GetArea import GetArea

class GetCountries(GetArea):
    def getCountryItems(self):
        content_area = GetArea().getContentArea()
        countries = []
        for country in content_area:
            country_items = country.find("a").get_text()
            countries.append(country_items)
        return countries