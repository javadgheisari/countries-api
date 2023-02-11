from django.shortcuts import render
# from rest_framework_mongoengine.generics import CreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
# from utils import get_db_handle
from django.http import HttpResponse
from django.views import View
from .models import Country
from .serializers import CountrySerializer, FindCountrySerializer
import requests
from .utils import MongoDB

db = MongoDB()

# db , cl = get_db_handle("SampleDB", "localhost", 27017, "abc123", "abc123")
# print(db)

class CountryView(APIView):
    def get(self, request):
        # country = Country(code=98, name="Iran", population=85, region="Asia").save()
        countries = Country.objects.all()
        # print(country)
        ser_data = CountrySerializer(instance=countries, many=True)
        return Response(ser_data.data)

    def post(self, request):
        ser_data = FindCountrySerializer(data=request.POST)

        if ser_data.is_valid():
            valid_data = ser_data.validated_data
            clean_name = valid_data['name'].lower().capitalize()
            print(clean_name)
            country = db.find_one("country", {"name": clean_name})
            if country:
                return Response(
                    {
                        "name":country['name'],
                        "code":country['code'],
                        "population":country['population'],
                        "region":country['region']
                    }
                )


            else:

                r = requests.get(f"https://restcountries.com/v3.1/name/{valid_data['name']}?fullText=true")

                if r.status_code == 200:
                    result = r.json()
                    country = Country(code=int(result[0]['idd']['root']+result[0]['idd']['suffixes'][0]), name=result[0]['name']['common'], population=int(result[0]['population']), region=result[0]['region']).save()
                    return Response(
                    {
                        "name":country['name'],
                        "code":country['code'],
                        "population":country['population'],
                        "region":country['region']
                    }
                )
                elif r.status_code == 404:
                    return Response({"message": "Not Found"})
                else:
                    return Response({"message": "Bad Request"})


            # countries = Country.objects.all()
            # for country in countries:
            #     if country['name'] == valid_data['name']:
            #         print(country)
            # # country = Country.objects(Q(name=valid_data['name']))
            #         if country:
            #                 return Response(
            #                     {
            #                         "name":country.name,
            #                         "code":country.code,
            #                         "population":country.population,
            #                         "region":country.region
            #                     }
            #                 )
            
        return Response({"message": "Bad Request"})
