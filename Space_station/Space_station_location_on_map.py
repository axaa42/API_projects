import folium #This library will be used to geographically map the location of the space station in real time
import requests
import json

#In this project we will map the real time coordinates of the space station

request=requests.get("http://api.open-notify.org/iss-now.json")#Calling the space station api
status_code = request.status_code#Too see if our request was success
reader=request.json()#Convert it to dictionary(pythn object)
print(reader)

#print(reader)#We now can access dic and get the data we want which is the position of the station

for key,value in reader.items():#We want to get long and lat
    if key== "iss_position":
        ll=value#as the value of long and lat are seperate dic we will store seperatly
lis=[float(value) for key,value in ll.items()]#We will convert the dic to lis of lon/lag

m = folium.Map(location=lis,zoom_start=12)#Location on map will be visulaised with folium mapping library in real-time
folium.Marker([lis[0],lis[1]],popup="SPACE STATION LOC",icon=folium.Icon('cloud'))#This will put a marker on the map for the location of the station


m.save('space_station.html')#This will save the file and show us where the station is on foliums map
