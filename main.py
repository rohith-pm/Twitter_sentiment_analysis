from flask import Flask, render_template, request
import tweepy
from tweepy import OAuthHandler
from textblob import TextBlob

app=Flask(__name__)

@app.route("/")
def index():
	return(render_template('form.html'))

@app.route("/result",methods=['GET','POST'])
def analyze():
	if request.method=='POST':
	
		#Accessing the twitter appi
		
		consumer_key="rQ3o7EtTFV9WaVNOFtcVQvyug"
		consumer_secret="Zj5owrsHxrLGFuoN4hTVOYJaD1hm3dgGh9zX9K2PClcOUMoLkr"
		access_token="1106372318987575296-lZekY2DUp3KXOzmcm8KWpRiG3QiEE5"
		access_token_secret="Z58W4UjuJTLVAVFE52ATDDRj7vHp3VcU7rOiACKCq6yeV"
		try:
			auth = OAuthHandler(consumer_key, consumer_secret)
			auth.set_access_token(access_token, access_token_secret)
			api = tweepy.API(auth)
		except:
			print("ERROR")
			
		#Acquiring the tweets with the keyword and count
		
		tweets = api.search(q = request.form["searchFor"], count = request.form["count"])
		p=0
		nu=0
		n=0
		
		#Sentiment analysis
		
		for tweet in tweets:
			analysis=TextBlob(tweet.text)
			if analysis.sentiment.polarity > 0:
				p+=1
			elif analysis.sentiment.polarity == 0:
				nu+=1
			else:
				n+=1
		print(p,nu,n)
		
		#return the results page
		
		return(render_template("result.html",pos=p,nut=nu,neg=n,cou=request.form["count"])) 

if __name__=="__main__":
    app.run(debug=True)