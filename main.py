import requests
from send_email import send_email
topic = "tesla"
api_key = "0807afcb8d864f828d7659fe2fce4720"

# news tesla
url = ("https://newsapi.org/v2/everything?"
       f"q={topic}&" 
       "from=2024-02-18&"
       "sortBy=publishedAt&"
       "apiKey=0807afcb8d864f828d7659fe2fce4720&"
       "language=en")

# make a request
request = requests.get(url)

# get a dictionary with data
content = request.json()

# Access the article  titles and description
body = ""
for article in content["articles"][:10]:
    if article["title"] is not None:
        body = body + article["title"] + "\n" + str(article["description"]) + 2 * "\n"

body = body.encode("utf-8")
send_email(message=body)


