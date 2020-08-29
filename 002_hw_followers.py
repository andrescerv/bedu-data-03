# Given a GitHub username, create a function to download all her/his followers' pictures.
from datetime import datetime
import requests


# CONSTANTS
URL_BASE = 'https://api.github.com/'


# FUNCTIONS
def get_github_user(username):
    url = f'{URL_BASE}users/{username}'
    response = requests.get(url)
    if response.status_code == 200:
        return(response.json())
    return None

def download_user_avatar(image_url):
    response = requests.get(image_url)
    if response.status_code == 200:
        response_content = response.content
        filename = f'tmp/{image_filename()}.png'
        with open(filename, 'wb') as image: 
            image.write(response_content)
            return filename
    return None

def image_filename():
    now = datetime.now()
    timestamp = datetime.timestamp(now)
    return timestamp

def download_github_followers_avatar(user):
    user_followers_url = user.get('followers_url') # URL with the JSON of the user's followers
    response = requests.get(user_followers_url)
    followers = response.json()
    for f in followers:
        follower_avatar_url = f.get('avatar_url')
        download_user_avatar(follower_avatar_url)

def count_github_followers(user):
    user_followers_url = user.get('followers_url') # URL with the JSON of the user's followers
    print(user_followers_url)
    response = requests.get(user_followers_url)
    data = response.json()
    print(response)
    n = len(data)
    return n

# IMPLEMENTATION
username = input('Give me the username:\t')
user = get_github_user(username) # JSON of user

if user:
    print(f'Github user "{username}" has {count_github_followers(user)} follower(s).')
    download_github_followers_avatar(user)
else:
    print('User not found')