from flask import Flask, render_template, request
import tweepy
import os
from dotenv import load_dotenv
import pandas as pd
#activamos el entorno para poder conectar el jupyter y extraer las variables
load_dotenv()


app = Flask(__name__)


API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET")


@app.route('/')
def index():
        auth = tweepy.OAuthHandler(API_KEY, API_SECRET) #Esta es la forma de autenticarnos mediante tweepy
        auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET) 
        api = tweepy.API(auth, wait_on_rate_limit=True)
        search = request.args.get('q')

        public_tweet = api.search(search, count=100, lang="en", exclude='retweets')
        
        return render_template('home.html', tweets=public_tweet)


if __name__=='__main__':
	app.run(debug=True)

