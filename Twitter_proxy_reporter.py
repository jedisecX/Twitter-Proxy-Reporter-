import tweepy
import requests
from itertools import cycle

# Define proxies
proxies = [
    "http://proxy1:port",
    "http://proxy2:port",
    "http://proxy3:port"
]
proxy_pool = cycle(proxies)

# Define multiple Twitter API credentials
accounts = [
    {"consumer_key": "", "consumer_secret": "", "access_token": "", "access_token_secret": ""},
    {"consumer_key": "", "consumer_secret": "", "access_token": "", "access_token_secret": ""},
    {"consumer_key": "", "consumer_secret": "", "access_token": "", "access_token_secret": ""},
    # Add as many accounts as needed
]

# Target username to report
target_username = "spam_account"

# Tweepy client with proxy support
def create_client(auth, proxy):
    session = requests.Session()
    session.proxies = {"http": proxy, "https": proxy}
    client = tweepy.Client(
        consumer_key=auth['consumer_key'],
        consumer_secret=auth['consumer_secret'],
        access_token=auth['access_token'],
        access_token_secret=auth['access_token_secret'],
        session=session
    )
    return client

# Report target user for spam
def report_user(client, username):
    user = client.get_user(username=username)
    if user:
        user_id = user.data.id
        response = client.report_user(user_id=user_id, reason="spam")
        print(f"Reported {username}: {response}")
    else:
        print(f"User {username} not found.")

# Main script
for account in accounts:
    proxy = next(proxy_pool)
    try:
        print(f"Using proxy {proxy}")
        client = create_client(account, proxy)
        report_user(client, target_username)
    except Exception as e:
        print(f"Error with account/proxy combination: {e}")
