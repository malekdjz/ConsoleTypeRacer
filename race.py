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
		char = stdscr.getch()
		if str(char) == str(snippet[index]):
			return True,char
		if str(char) == "27":
			quit()
		else:
			return False,char

##########################################################################################

def typing(snippet,y,x):
	curses.noecho()
	stdscr.move(0,0)
	curses.init_pair(1,curses.COLOR_GREEN,curses.COLOR_BLACK)
	index = 0
	for char in snippet:
		while True :
			test,c = compare_char(snippet, index)
			if test:
				stdscr.addch(chr(c),curses.color_pair(1))
				stdscr.refresh()
				index = index +1
				curr_y,curr_x = stdscr.getyx()
				stdscr.addstr(y+2,x,str(index))
				stdscr.move(curr_y,curr_x)
				break

##########################################################################################


##########################################################################################

def random_snippet(json_string):
	snippet = str(random.choice(json_string))
	return snippet

##########################################################################################

def open_json(lang):
	path = "snippets/"+lang+"_snippets.json"
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
		stdscr.addstr(str(snippet))
		stdscr.refresh()
	except:
		print("The console needs to be bigger")
		quit()
	stdscr.addch('\n')
	y,x = stdscr.getyx()
	return y,x

##########################################################################################

def main():
	stdscr.clear()
	json_string = open_json("python")
	snippet = random_snippet(json_string)
	y,x = print_snippet(snippet)
	typing(snippet,y,x)

##########################################################################################

if __name__ == "__main__":
	stdscr = curses.initscr()
	curses.start_color()
	main()
