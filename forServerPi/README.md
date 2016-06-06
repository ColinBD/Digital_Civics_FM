All the files contained in this folder will be loaded onto the Pi housed within our server. 

The job this Pi does is to:
	1. Scrape social media every 10 minutes (exact time interval to be confirmed)
	2. Scrape the last 20 tweets involving @uniofnewcastle (the university's official feed) and:
		a) Parse it to make it more readable
		b) Output the text to an XML file
		c) Send the XML file into a text to speech convertor which outputs an audio file of the tweets being read
		b) Pressing play, stop or eject
	3. As above using a hash tag related to the participants chosen special interest field (for the purpose of this demonstration we shall use @IVFresearch which one of our workshop participants expressed a keen interest in)
	4. Scrape facebook and proceed as above
	5. Scrape instagram and proceed as above
	6. Push the resulting audio files and scraped image files to the raspberry pi housed in the radio 
