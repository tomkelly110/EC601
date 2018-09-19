#!/usr/bin/env python
import tweepy
import json
con_key = "Consumer key"
con_sec = "Consumer secret key"
acc_key = "Access key"
acc_sec = "Access secret key"

def digest(username):
	keyring = tweepy.OAuthHandler(con_key, con_sec)
	keyring.set_access_token(acc_key, acc_sec)
	tweetapi = tweepy.API(keyring)
	tweetlist = []
	tweetlist = tweetapi.user_timeline(screen_name = username, count = 5)
	print(tweetlist[0].text)
	#seperate out images
	#put images into video
	#put video into vision
	#output vision text


if __name__ == '__main__':
	con_key = input("Hello and welcome to this version of MiniProject 1.\nThis module was coded by Thomas Kelly.\nPlease enter your Consumer Key.\n")
	con_sec = input("Please enter your Consumer Secret Key\n")
	acc_key = input("Please enter your Access Key\n")
	acc_sec = input("Please enter your Access Secret Key\n")
	flag = 1
	targetname = "@BarackObama"
	while flag > 0:
		targetname = input("Please enter the desired twitter handle, including the @ symbol\n")
		digest(targetname)
		if input("Would you like to see any other twitter handles? (y/n)\n") != "y":
			flag = 0