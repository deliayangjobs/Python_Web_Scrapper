import requests
from bs4 import BeautifulSoup
import pandas

r=requests.get("http://www.century21.com/real-estate/foster-city-ca/LCCAFOSTERCITY/?")
c=r.content

soup=BeautifulSoup(c, "html.parser")

all=soup.find_all("div",{"class":"property-card-primary-info"})
#first_price=all[0].find("a",{"class":"listing-price"}).text.replace("\n","").replace(" ","")

#length=len(all)

#df=pandas.DataFrame(columns=["Price", "Address", "Locality", "Beds", "Baths", "Half-Baths"])
l=[]
for item in all:
    d={}
    d["Price"]=item.find("a",{"class":"listing-price"}).text.strip()
    d["Address"]=item.find("div",{"class":"property-address"}).text.strip()
    d["Locality"]=item.find("div",{"class":"property-city"}).text.strip()

    try:
        d["Beds"]=item.find("div",{"class":"property-beds"}).find("strong").text
    except:
        d["Beds"]=None

    try:
        d["Baths"]=item.find("div",{"class":"property-baths"}).find("strong").text
    except:
        d["Baths"]=None

    try:
        halfBath=item.find("div",{"class":"property-half-baths"})
        d["Half-Baths"]=halfBath.find("strong").text if halfBath!=None else '0'
    except:
        d["Half-Baths"]=None
    l.append(d)

df=pandas.DataFrame(l)

df.to_csv("century21.csv")
#print(df)
#print(l)
