import requests

#THIS IS HOW TO CALL A EBAY API WITH SEARCH
r="xxx"#This is the token
headers={"Authorization":r}#This is the auth
#THE FOLLowing IS THE EBAY API.NOTE THAT YOU CAN PUT & TO GET THE ITEM YOU WANT
d="""https://svcs.ebay.com/services/search/FindingService/v1?OPERATION-NAME=findItemsByKeywords&RESPONSE-DATA-FORMAT=JSON&keywords=arsenal&SECURITY-APPNAME=xxx&paginationInput.entriesPerPage=25&paginationInput.pageNumber=1&GLOBAL-ID=EBAY-US"""#This is the url for ebay api.note that products per page and number of entries are put as queries.also you have to get appid which is in developer.also note you have to put what kind of api endpoint it is
#FOLLWOING ARE ANOTHER WAY OF PUTTING PARAMENTES IN THE URL
g=request = {
    'paginationInput': {
        'entriesPerPage': 20,
        'pageNumber': 1
    }
}
dic={}
#tHE FOLLWOING WILL GET THE DATA
response=requests.get(d)#Will pull the data
c=response.json()#Will convert to json data
#The following gets the names of the products
#the follwoing will get the name from our search
for key,value in c.items():
    f=value
for x in f:
    d=x["searchResult"]
for x in d:
    cx=x["item"]
for x in cx:
    print(x["title"])
    

print(f)
for x in f:
    print(x["searchResult"][0]["item"][0]["title"]) #this will get the searchresult,item and tile of the item.
    
    
for item in response.reply.c.item:
    print(f"Title: {item.title}, Price: {item.sellingStatus.currentPrice.value}")#This will get title and price

