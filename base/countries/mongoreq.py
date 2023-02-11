from .models import Country

country = Country(countryid=98, name="Iran", people=85, continent="Asia").save()

print(country.countryid)