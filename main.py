import requests

api_key = "0807afcb8d864f828d7659fe2fce4720"

# news tesla
url = ("https://newsapi.org/v2/everything?q=tesla&" 
       "from=2024-02-18&sortBy=published" 
       "At&apiKey=0807afcb8d864f828d7659fe2fce4720")

# make a request
requests = requests.get(url)

# get a dictionary with data
content = requests.json()

# Access the article  titles and description
for article in content["articles"]:
       print(article["title"])
       print(article["description"])

