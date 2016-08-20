#!usr/bin/env python

import tweepy
import MySQLdb
import time
import json
from tweepy import Stream 
from tweepy.auth import OAuthHandler
from tweepy.streaming import StreamListener 

ckey='dH7wGLT9ZQp7pA9QBKxq6hBXE'
csecret='U0ZkvQ21dQw8zQ4VnvvOrK0DS5MDKB0gRDyYpyCp8w7FESXqOQ'
atoken='3181521055-tfcxyBJwQ2nHYQIhfbRR0wBvSga2IHfJKlbzKC6'
asecret='Qv6sYaSJ45xL6Tp1jvpSaT5YobH6rGhSVzkfE2r5svALB'
 
	
class listener(StreamListener):
  def __init__(self):
	self.host="localhost"
	self.user="root"
	self.password='123'
	self.db="sentimen"

  def on_data(self,data):
	koneksi=MySQLdb.connect(self.host,self.user,self.password,self.db)
	c=koneksi.cursor()
	try :
		all_data=json.loads(data)
		tweet=all_data["text"]
		username=all_data["user"]["screen_name"]
		c.execute("INSERT INTO `tweets`(`time`,`username`,`tweet`)VALUES(%s,%s,%s)",(time.time(),username,tweet))
		print (username,tweet.encode('latin-1'))
	except MySQLdb.Error, e :
		print "ERROR %d IN CONNECTION: %s" % (e.args[0],e.args[1])
  def on_error(self,status): 
	print status
auth=OAuthHandler(ckey,csecret)
auth.set_access_token(atoken,asecret)
twitterStream=Stream(auth,listener())
twitterStream.filter(track=["ahok"])
