import requests
#import sys 
import sys, locale, os

url = ('https://newsapi.org/v2')
apiKey = "cfd6c67f287848e895900e49af8e4ab6"
countries = {
"United Arab Emirates" : "ae",
"Argentina" : "ar",
"Austria" : "at",
"Australia" :"au",
"Belgium" : "be",
"Bulgaria" : "bg",
"Brazil": "br",
"Canada" : "ca",
"Switzerland": "ch",
"China" : "cn",
"Colombia" : "co",
"Cuba" : "cu",
"Czech Republic" : "cz",
"Germany" : "de",
"Egypt" :"eg",
"Spain" :     "es",
"France" :   "fr",
"United Kingdom" :   "gb",
"Greece" :   "gr",
"Hong Kong" :   "hk",
"Hungary" :   "hu",
"Indonesia" :    "id",
"Ireland" :   "ie",
"Israel" :   "il",
"India" :   "in",
"Iceland" :   "is",
"Italy" :   "it",
"Japan":   "jp",
"Korea, Republic of"   : "kr",
"Lithuania" :     "lt",
"Latvia" :    "lv",
"Morocco" :   "ma",
"Mexico" :    "mx",
"Malaysia" :    "my",
"Nigeria" :    "ng",
"Netherlands" :    "nl",
"Norway" :   "no",
"New Zealand" :    "nz",
"Philippines" :    "ph",
"Pakistan" :    "pk",
"Poland":    "pl",
"Portugal" :    "pt",
"Romania":    "ro",
"Serbia" :    "rs",
"Russian Federation" :    "ru",
"Saudi Arabia" :    "sa",
"Sweden" :    "se",
"Singapore" :    "sg",
"Slovenia" :    "si",
"Slovakia"   : "sk",
"Thailand":    "th",
"Turkey" :    "tr",
"Taiwan, Province of China" :  "tw",
"Ukraine" :   "ua",
"United States" :   "us",
"Venezuela, Bolivarian Republic of":   "ve",
"South Africa"  : "za",
}
categories = {"business", "entertainment", "general", "health", "science", "sports", "technology"}


def search_by_country(country):
    if(country in countries):
        urlcountry = url +  '/top-headlines?country='+countries[country]+"&apiKey="+apiKey
        response = requests.get(urlcountry)
        #response.encoding = 'utf-8'

        print(response.json())
    else : 
        print("not existing country")
def search_by_topic(topic):
    if(topic in categories):
        urltopic = url + '/everything?q=' + topic +'&apiKey='+apiKey
        response = requests.get(urltopic)
        print(response.json())

search_by_country('United States')
search_by_topic('bitcoin')