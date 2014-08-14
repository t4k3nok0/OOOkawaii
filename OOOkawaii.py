# -*- coding: utf-8 -*-

import tweepy
from random import randrange

consumer_key    = ""
consumer_secret = ""
access_key      = ""
access_secret   = ""

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

list1 = ["","めっちゃ","超","すごく","普通に"]
rand = randrange(0,4)
jyo = list1[rand]
kaz = int(0)

kaisu = input("何回かわいいする？: ")

for var in range(0, kaisu):
	
	kaz = int(kaz)
	kaz = kaz + int(1)
	kaz = str(kaz)

	#OOOは適語に置き換えてください
	print "ＯＯＯ%sかわいい！！ (%s回目)" % (jyo,kaz)




