
import tweepy
import MySQLdb
import time
import json
from tweepy import Stream 
from tweepy.auth import OAuthHandler
from tweepy.streaming import StreamListener 

conn = MySQLdb.connect("localhost","root","123","sentimen")
c = conn.cursor()


ckey='dH7wGLT9ZQp7pA9QBKxq6hBXE'
csecret='U0ZkvQ21dQw8zQ4VnvvOrK0DS5MDKB0gRDyYpyCp8w7FESXqOQ'
atoken='3181521055-tfcxyBJwQ2nHYQIhfbRR0wBvSga2IHfJKlbzKC6'
asecret='Qv6sYaSJ45xL6Tp1jvpSaT5YobH6rGhSVzkfE2r5svALB'
 
	
class listener(StreamListener):

    def on_data(self, data):
        all_data = json.loads(data)
        
        t = all_data["text"]
        tweet=t.encode('utf-8')
        waktu=time.time()
        username = all_data["user"]["screen_name"]
        c.execute("INSERT INTO `tweets`(`time`, `username`, `tweet`) VALUES (%s,%s,%s)",
            (time.time(), username, tweet))

        conn.commit()
        print((username,tweet))
        
        return True

    def on_error(self, status):
        print status

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["ahok"])
