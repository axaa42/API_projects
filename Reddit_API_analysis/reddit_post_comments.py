import requests
import pandas

#THIS PROJECT WILL GET COMMENTS OF REDDIT POSTS AND WE WILL USE THIS AS TRAINING DATA.

base_url = 'https://www.reddit.com/' #Reddit url

#The following is the security to get to our username in reddit
data = {'grant_type': 'password', 'username': "xxx", 'password': "xxx"}

#The following is the secret key and id for reddit which is given when makin the app
auth = requests.auth.HTTPBasicAuth("xxx", "xxx")

#This will give us a token which we can use instead of typing a pass and username
#the base url is reddit, the data is our account info, the headers is who is doing it,
#auth is what will connect to our account

r = requests.post(base_url + 'api/v1/access_token',
                  data=data,
                  headers={'user-agent': 'xxx'},
		  auth=auth)



a=r.json()# Convert it to json
print(a)


token = 'bearer ' + a["access_token"] #This is how to represent the token(we will use token from lis)

base_url = 'https://oauth.reddit.com'#Now we have to add ouath for token.Note we use OAUTH becasue it is constant

headers = {'Authorization': token, 'User-Agent': 'xxx'}#We add token and user like this
response = requests.get("https://oauth.reddit.com/r/Showerthoughts/comments/awi9q3/xxx/",
                        headers=headers,
                        params={"limit":100,"sort":"top"})
s=response.json()#Convert it to json

s=s[1:]#The first part in list is the subreddit info.which we dont want

for x in s:
    xc=x["data"]["children"]#This will get the data and children which has the info we want



dic={}#we want to store the comments of the post as keys and likes a values
for x in xc:
    c=x["data"]#This will get the data where the info of comment and stuff is
    if "body" in c:#In some of the dictionaries there is no body.so if there is then okay otherwise there will be error
        dic[c["body"]]=c["ups"]#Making a dictionary
print(dic)
    


    


            
