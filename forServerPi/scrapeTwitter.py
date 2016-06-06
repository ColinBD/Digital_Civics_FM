#written by Colin Dodds

import twythonTool
import txt2wavTool
import subprocess

#run the script that scrapes the latest Newcastle Uni tweets, parses them and then saves them into an XML file
twythonTool

#run the script that takes our tweets in XML format and converts them to an audio file
#txt2wavEx.py -L licence.lic -V heather.voice tweets.xmltxt2wavEx(-L licence.lic,-V heather.voice,tweets.xml)
return_code = subprocess.call(["python", "txt2wavTool.py", "-L", "licence.lic", "-V", "heather.voice", "tweets.xml"])



