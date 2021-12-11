import requests
import pandas as pd

#The following code will get real-time weather information

#insert own api key in the link
#THE FOLLWOING WILL GET THE FORECASTR DATA FOR NEXT 3 DAYS FOR 3 HOUR INTERVALS
r=requests.get("xxxxxxxxxxxx")
a=r.json()#CONVERT TO JSON
#print(a)
for key,value in a.items():#GET ONLY LIST AS THAT IS WHERE OUR DATA IS
    if key =="list":
        c=value #C varaible holds the data
#print(c[0])#USE THIS AS A GUIDE TO SEE HOW DATA IS STRUCRRED
print("------")


forecast=top_today=df = pd.DataFrame({'date': [],"type":[],"temp":[]})#making a dataframe which we will use to upload the date, type and temprature of the weather
for x in c:
    r=x["main"]#we want main where our data is in
    g=x["weather"]#we want to access data from here
    f=x["main"]["temp"]#this will get temp
    
    #Below will get the date and type of weather and temperature in to a df 
    forecast = forecast.append({'date': x["dt_txt"],"type":g[0]["main"],"temp":f}, ignore_index=True) 


forecast["date"]=pd.to_datetime(forecast["date"])#this will convert the datetime column to datatime so we can do analysis on it
print(forecast)

