# coding: utf-8
# Importing the modules
import sys
import string
import re #used when removing url info
from twython import Twython

#Set twitter details - you will need to add your own here to use this file
app_key = "redacted"
app_secret = "redacted"
oauth_token = "redacted"
oauth_token_secret = "redacted"

#Set-up twitter
twitter = Twython(app_key, app_secret, oauth_token, oauth_token_secret)

results = twitter.search(q='#breastfeeding', count=20)

#write tweets to an XML file - this is what the text to speech software requires as input
file = open("special_interest_tweets.xml", "w")
#set-up the XML file
file.write("<?xml version='1.0'?>" + "\n" + "<parent>" + "\n") 

#write the tweets
for result in results['statuses']:
  output = result["text"].encode("utf-8")

  #Parse the tweets to make them clearer when read out by the text to speech process
  parse1 = output.replace('RT', 'retweet ')
  parse2 = parse1.replace('@UniofNewcastle', 'at uni of newcastle')
  parse3 = parse2.replace('#', 'hash tag ')
  parse4 = parse3.replace('&amp;', 'and')
  #parse5 = parse4.replace('https://', 'u r l ') 
  parse5 = re.sub(r"(?:\@|https?\://)\S+", "", parse4) # strip out URLs to make the speech clearer
  #print parse5
  
  file.write (parse5 + '\n' + '\n')

#complete the XML file
file.write("</parent>")
file.close()
