import requests

response = requests.get('https://jsonplaceholder.typicode.com/posts')
posts = response.json()
# print(response.json())

for post in posts:
    print(post['id'], post['title'])