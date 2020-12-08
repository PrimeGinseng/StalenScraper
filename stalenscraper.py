# stalenscraper.py
# Description: Rips every image from http://www.simonstalenhag.se/
import os
import urllib
import urllib2
from bs4 import BeautifulSoup

url = "http://www.simonstalenhag.se/";

content = urllib2.urlopen(url).read()
soup = BeautifulSoup(content)

print soup.prettify()

images = soup.find_all("a")
newimage = ""

# Simon's got his images shown several cut sections, so isolate the image's url
# as it will repeat for each section.
for highres in images:
	if newimage == "":
		newimage = highres.get('href')
	else:
		if highres.get('href') != newimage:
			newimage = highres.get('href')
			print newimage
			imgURL = "http://www.simonstalenhag.se/" + str(newimage)
			urllib.urlretrieve(imgURL, os.path.basename("/Simon Stalenhag/" + imgURL))