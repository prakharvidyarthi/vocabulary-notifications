from bs4 import BeautifulSoup
from random import randint
import urllib2
import os
import time

def message(title, message):
  os.system('notify-send "'+title+'" "'+message+'"')

page = urllib2.urlopen('https://www.vocabulary.com/lists/197265#view=notes').read();

parsed = BeautifulSoup(page)

word = []
meaning = []

site_meanings = parsed.find_all("div" , class_="definition")

site_words = parsed.find_all("a",class_="word dynamictext")

print(site_words)

for site_word in site_words:
	word.append(site_word.get_text().encode("utf-8"))

for site_meaning in site_meanings:
	meaning.append(site_meaning.get_text().encode("utf-8"))

while(1):
	i = randint(0,90)

	message("New word",word[i])

	time.sleep(15)

	message("Word : " + word[i],meaning[i])

	time.sleep(600)