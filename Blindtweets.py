#!/usr/bin/env python
import tweepy
import json
import requests
from google.cloud import vision
from google.cloud.vision import types
from PIL import Image
from io import BytesIO
from subprocess import Popen, PIPE
con_key = "Consumer key"
con_sec = "Consumer secret key"
acc_key = "Access key"
acc_sec = "Access secret key"
amount = 10

def digest(username):
	keyring = tweepy.OAuthHandler(con_key, con_sec)
	keyring.set_access_token(acc_key, acc_sec)
	tweetapi = tweepy.API(keyring)		#Authenication
	tweetlist = []
	tweetlist = tweetapi.user_timeline(screen_name = username, count = amount) #get tweets
	media_files = set()
	for status in tweetlist:			#go through all tweets
		media = status.entities.get('media', [])	#see if there is an image
		if(len(media) > 0):
			media_files.add(media[0]['media_url'])	# if so save its url to list
	client = vision.ImageAnnotatorClient()
	image = vision.types.Image()
	p = Popen(['ffmpeg', '-y', '-f', 'image2pipe', '-vcodec', 'mjpeg', '-r', '1/2', '-i', '-', '-vcodec', 'mpeg4', '-q:a', '5', '-r', '24', '%s.avi' % (username)], stdin=PIPE) #sets up ffmpeg pipe, overwrites output, changes format, framerate is 1/2
	textfile = open("%s.txt" % (username),"w+") #create text file
	for media_file in media_files:			#for all the image urls in the list
		textfile.write("\n\nImage: ")			#write header for each image (url) to text file
		textfile.write(media_file)
		image.source.image_uri = media_file
		response = client.label_detection(image=image) #send to google vision and get response
		labels = response.label_annotations
		for label in labels:
			textfile.write("\n")		#write labels to the text file
			textfile.write(label.description)
		imageresponse = requests.get(media_file)	#request image from url
		img = Image.open(BytesIO(imageresponse.content)) #open as image object
		img.save(p.stdin, 'JPEG')				#send into pipe to get to ffmpeg
	p.stdin.close()					#close resources
	p.wait()
	textfile.close() 

if __name__ == '__main__':
	con_key = input("Hello and welcome to this version of MiniProject 1.\nThis module was coded by Thomas Kelly.\nPlease enter your Consumer Key.\n")
	con_sec = input("Please enter your Consumer Secret Key\n")
	acc_key = input("Please enter your Access Key\n")
	acc_sec = input("Please enter your Access Secret Key\n")
	flag = 1
	targetname = "@NatGeoPhotos"
	while flag > 0:
		targetname = input("Please enter the desired twitter handle, including the @ symbol\n")
		try:
			amount = int(input("Please enter the number of tweets to process\n"))
			digest(targetname)
		except Exception as issue:
			print("There was an error")
			print(type(issue))
		if input("Would you like to see any other twitter handles? (y/n)\n") != "y":
			flag = 0