import curses
import requests
import json
import random

def compare_char(snippet,index):
	try:
		snippet = snippet.encode("ascii")
	except:
		print("Something went wrong ")
	else :
		char = str(stdscr.getch())
		if char == str(snippet[index]):
			return True
		if char == "27":
			quit()
		else:
			return False
##########################################################################################

def typing(snippet):
	curses.noecho()
	index = 0
	for char in snippet:
		while True :
			test = compare_char(snippet, index)
			if test:
				index = index +1
				break

##########################################################################################

def random_snippet(json_string):
	snippet = str(random.choice(json_string))
	return snippet

##########################################################################################

def open_json(lang):
	path = lang+"_snippets.json"
	try:
		f = open(path,"r")
	except:
		print("file doesn't exist")
		quit()
	else:
		json_string  = json.load(f)
		return json_string

##########################################################################################

def print_snippet(snippet):
	try:
		for char in snippet:
			stdscr.addch(str(char))
			stdscr.refresh()
	except:
		print("The console needs to be bigger")
		quit()
	stdscr.addch('\n')

##########################################################################################

def main():
	stdscr.clear()
	json_string = open_json("python")
	snippet = random_snippet(json_string)
	print_snippet(snippet)
	typing(snippet)

##########################################################################################

if __name__ == "__main__":
	stdscr = curses.initscr()
	main()
