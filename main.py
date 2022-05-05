import tweepy
import random
import requests
import os
from multiprocessing import Process
import time

print('----------------------------------')
print('----------------------------------')
print('     _                   _          _   \n ___| |_  ___  _ _  ___ | |__  ___ | |_ \n(_-/|  _|/ -_)| \'_|/ -_)|  _ \/ _ \|  _|\n/__/ \__|\___||_|  \___||____/\___/ \__|\n')

print('Starting...')

auth = tweepy.OAuthHandler(os.environ['auth1'], os.environ['auth2'])
auth.set_access_token(os.environ['auth3'], os.environ['auth4'])

print('Connected')

api = tweepy.API(auth)

def news():
    print('News mode')
    response = requests.get('https://newsapi.org/v2/top-headlines?country=fr&apiKey='+os.environ['news1']).json()
    if response['status']=="ok":
        articles=response['articles']
        articlet = random.randint(0, len(articles)-1)
        article = articles[articlet]
        api.update_status(
         #'Nouvel article par '+article['source']['name']+" -> "+
          "#news "+article['title']+" "+article['url'])
        print('Tweeted')
    else:
        print('ERROR NEWS')

import http.server
import socketserver

PORT = 8082
Handler = http.server.SimpleHTTPRequestHandler


def serve():
  with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()

        
def tweet():
  while(True):
    sec = random.randint(7000, 13000)
    print('--------------------------------------')
    news()
    print('See you in', sec)
    time.sleep(sec)


p = Process(target=serve)
p.start()

v = Process(target=tweet)
v.start()
v.join()
