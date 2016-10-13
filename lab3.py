#sub problems
#1. parse csv file and extract data
#2. choose correct data structure to store data
#3. calculate distance b/w 2 points using the Great circle distance formula

import csv
myfile= open('GeoLiteCity-Location.csv','rb')
reader = csv.reader(myfile)
count = 0
myMap = {}
for row in reader:
     
     if count < 2:
         count += 1
         continue
     locId, country, region, city, postalCode, latitude, longitude, metroCode, areaCode = row
     
     if not(locId==""):
         myMap[latitude,longitude]=city
         
choice= input ("Enter 1 to search by name or 2 to search by latitude/ longitude")
if  choice == 1:
    name=input ("Enter the name of the city")
elif choice == 2:
    lat=input ("Enter latitude: ")
    long= input("Enter longitude:")

num= input("Enter the number of nearby cities to search:")


     
        
          