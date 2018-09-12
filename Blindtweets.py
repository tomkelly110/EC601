#!/usr/bin/env python
import tweepy
import json
con_key = "Consumer key"
con_sec = "Consumer secret key"
acc_key = "Access key"
acc_sec = "Access secret key"

def digest(username):
	print(username)
	#authorize to twitter
	#put tweets in list
	#seperate out images
	#put images into video
	#put video into vision
	#output vision text


if __name__ == '__main__':
	con_key = input("Hello and welcome to this version of MiniProject 1.\nThis module was coded by Thomas Kelly.\nPlease enter your Consumer Key.\n")
	con_sec = input("Please enter your Consumer Secret Key\n")
	acc_key = input("Please enter your Access Key\n")
	acc_sec = input("Please enter your Access Secret Key\n")
	print(con_key+con_sec+acc_key+acc_sec)
	flag = 1
	targetname = "@BarackObama"
	while flag > 0:
		targetname = input("Please enter the desired twitter handle, including the @ symbol\n")
		digest(targetname)
		if input("Would you like to see any other twitter handles? (y/n)\n") != "y":
			flag = 0