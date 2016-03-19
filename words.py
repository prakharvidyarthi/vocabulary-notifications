from bs4 import BeautifulSoup
from random import randint
import urllib2
import os
import time

def message(title, message):
  os.system('notify-send "'+title+'" "'+message+'"')

word = []
meaning = []

for i in range(1,15):
	page = urllib2.urlopen('http://www.majortests.com/gre/wordlist_0' + str(i)).read();

	parsed = BeautifulSoup(page, "lxml")

	site_meanings = parsed.find_all("td")

	site_words = parsed.find_all("th")

	for site_word in site_words:
		word.append(site_word.get_text().encode("utf-8"))

	for site_meaning in site_meanings:
		meaning.append(site_meaning.get_text().encode("utf-8"))

while(1):
	i = randint(0,len(word)-1)

	message("Word : " + word[i],meaning[i])

	time.sleep(120)
