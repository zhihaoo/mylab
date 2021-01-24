#!/usr/bin/python
#This file scrape through all txt file and list the following:
#1) 2207 class playlist
#2) github username
#3) github link for lab01 part 1



#import modules(s)
import sys
import re
import os
import json
from pprint import pprint as pprint

#global variable

#to read file
def extraction(filename):
	with open(filename,'r', errors='ignore') as f:
		textArray = [l.rstrip("\n") for l in f]
	f.close()
	basename = (filename.split('.')[0])
	userinformation_dict = {}
	userinformation_dict[basename] = {}
	userinformation_dict[basename]['playlist'] = textArray[0]
	userinformation_dict[basename]['github_username'] = textArray[1]
	try:
		userinformation_dict[basename]['remoterepo'] = textArray[2]
	except IndexError:
		userinformation_dict[basename]['remoterepo'] = 'NULL'
#	pprint userinformation_dict
	return userinformation_dict


#to write file
def fileoutput(content):
	with open('2207_userlist.json', 'a') as f:
		f.write(json.dumps(content))
	f.close()
	print("output > 2207_userlist.json")

#main
def main():
	classDict = {}

	if len(sys.argv) < 2:
		print("Usage: scrapper.py <filename>")
		exit()

#	filename = sys.argv[1]
#	userDict = extraction(filename)

	filename_list = os.listdir()
	for filename in filename_list:
		if filename.endswith('.txt'):
			userDict = extraction(filename)
			classDict.update(userDict)

#	pprint(classDict)
	fileoutput(classDict)

if __name__=="__main__":
	main()
