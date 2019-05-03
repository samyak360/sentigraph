#!/usr/bin/python3

import  tweepy
import  sys
import matplotlib.pyplot  as  plt
from  textblob  import TextBlob

topic=sys.argv[1]

consumer_key='HpFC6iUO0s6cEI0FuSYZKfLEE'
consumer_sec='BKcMn1uduQbXIIhIRcWkTAZ8vIrw2jWM98GpLwyKhBQc13q0Vw'
#  by using above keys  we are going to check auth handler 

auth=tweepy.OAuthHandler(consumer_key,consumer_sec)
#  here auth is token by consuker key and sec 

access_key='1667627228-36SVYJOWnkSHpDHaWY2qbji9OK6YLZ0PXOPIF49'
secret_key='HlIKAIZVV4jK3dPUqYF0xRZDdmQAC4r1WTlouZRQkYrJr'
#  connecting  data server  with  access and secret key  by using above token

auth.set_access_token(access_key,secret_key)

#  connecting to twitter api with  token that is stored in auth
connected=tweepy.API(auth,wait_on_rate_limit=True)

#  searching topics 
tweet=connected.search(topic,count=100)

#  converting into text
x=[]
a=[]
b=[]
y=[]

for  j  in  tweet:
	analize=TextBlob(j.text)
	x.append(analize.sentiment.polarity)
	y.append(analize.sentiment.subjectivity)

for i in range(len(x)):
	a.append(i)
	b.append(i)

plt.xlabel("tweet no.")
plt.ylabel("polarity")
plt.scatter(a,x,s=20)
plt.plot(a,x,label="polarity plot")
plt.legend()
plt.grid()

plt.xlabel("tweet no.")
plt.ylabel("subjectivity")
plt.scatter(b,y,s=20)
plt.plot(b,y,label="subjectivity plot")
plt.legend()
plt.grid()
plt.show()



