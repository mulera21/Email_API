import requests

api_key = "0807afcb8d864f828d7659fe2fce4720"

url = ("https://newsapi.org/v2/everything?q=tesla&" 
       "from=2024-02-18&sortBy=published" 
       "At&apiKey=0807afcb8d864f828d7659fe2fce4720")

requests = requests.get(url)

content = requests.text
print(content)
