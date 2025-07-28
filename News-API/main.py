import requests # pip3 install requests

query = "Software Development"
api_key ="" #add your own api key here from https://newsapi.org/

url= f"https://newsapi.org/v2/everything?q={query}&from=2025-06-28&sortBy=publishedAt&apiKey={api_key}"
print(url)

content = requests.get(url)
data = content.json()
articles = data['articles']


# enumerate returns index along with the article here
for index, article in enumerate(articles):
  print(f"Article {index + 1}:")
  print(f"Title: {article['title']}")
  print(f"URL: {article['url']}")
  print(f"Description: {article['description']}")
  print('\n*************************************\n')