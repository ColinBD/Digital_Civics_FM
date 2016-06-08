#written by Colin Dodds

import twythonSpecialInterestTool
import txt2wavTool
import subprocess

#run the script that scrapes the latest breastfeeding tweets, parses them and then saves them into an XML file
twythonSpecialInterestTool

#run the script that takes our tweets in XML format and converts them to an audio file
return_code = subprocess.call(["python", "txt2wavTool.py", "-L", "licence.lic", "-V", "heather.voice", "special_interest_tweets.xml"])



