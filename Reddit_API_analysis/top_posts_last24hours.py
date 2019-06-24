import requests
import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

####THIS PROJECT WILL GET TOP POSTS OVER LAST 24 HOURS AND WE WILL MAKE A DATABASE OF IT AND
####MAKE A SUBPLOT LOOKING AT ITS UPVOTES AND THE SUBREDDIT
###We will then use this scraped data for analysis

base_url = 'https://www.reddit.com/' #Reddit url
#The following is the security to get to our username in reddit
data = {'grant_type': 'password', 'username': "xxx", 'password': "xxx"}
#The following is the secret key and id for reddit which is given when makin the app
auth = requests.auth.HTTPBasicAuth("xxx", "xxx")
#This will give us a token whihc we can use instead of typing a pass and username
#the base url is reddit, the data is our account info, the headers is who is doing it,
#auth is what will connect to our account

r = requests.post(base_url + 'api/v1/access_token',
                  data=data,
                  headers={'user-agent': 'xxx'},
		  auth=auth)

d = r.json()#This will give us our token in json format
print(d)

#MAKE PANDAS WITH POST AND LIKES IN ANOTHER COLUMN

token = 'bearer ' + d["access_token"]#This is how to represent the token(we will use token from lis)
#NOTE THE TOKEN EXPIRES AFTER A WHILE.AND A NEW ONE WILL BE GIVEN THROUGH REQUEST.POST
base_url = 'https://oauth.reddit.com'#Now we have to add ouath for token

headers = {'Authorization': token, 'User-Agent': 'xxx'}#We add token and user like this

response = requests.get("https://oauth.reddit.com/r/popular/top/", headers=headers,
                        params={"limit":200,"t":"day"})#note when you go on reddit.and click on something

j=response.json()#Convert it to json                            #Copy the link and filter by top and etc like in here  
data=j["data"]["children"]#We only want the data and children part of json file
top_today=df = pd.DataFrame({'subreddit': [],"ups":[],"title":[]})#We want top in last 24 hours and this will make a dataframe to do so
for x in data:
     top_today = top_today.append({'subreddit': x["data"]["subreddit"],"ups":x["data"]["ups"],
                            "title":x["data"]["title"]}, ignore_index=True)#This will add it to dataframe
print(top_today.loc[:,["title","ups"]])
#Now we have a dataframe with the subreddit, the title and the upvotes of each post which we can use to analyse


###NOW WE WILL PUT THE DATAFRAME INTO A DATABASE WHICH IN THIS CASE IN SQLITE3
conn = sqlite3.connect("24_hour_reddit.db")#This will make a new database

#convert_p_sql=top_today.to_sql('top_reddit', conn, if_exists='replace', index=False)#This will convert to sql

#The following will let us execute sql commands from python
cursor = conn.cursor()
cursor.execute("select * from top_reddit ")#To execute sql commands
f=cursor.fetchall()

g=pd.read_sql('select * from top_reddit limit 5', conn)##This will convert sqlite3 commandas in pandas

lines = g.plot(kind="bar")#We will make a bar plot with upvotes
lines.set_xticklabels(g["subreddit"])#This will set x-axis to its subreddit
print(g.loc[:,["subreddit","ups"]])


print(lines) 
conn.close()







