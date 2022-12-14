import curses
import json
import random
import time
from pyfiglet import Figlet
def compare_char(snippet,index):
	try:
		snippet = snippet.encode("ascii")
	except:
		print("Something went wrong ")
		return False,False
	else :
		char = stdscr.getch()
		if char == snippet[index]:
			return True,char
		if char == 27:
			quit()
		else:
			return False,False


def typing(snippet,y,x):
	curses.noecho()
	stdscr.move(2,0)
	curses.init_pair(1,curses.COLOR_GREEN,curses.COLOR_BLACK)
	index = 0
	t = 0
	for char in snippet:
		while True :
			test,c = compare_char(snippet, index)
			if test:
				stdscr.addch(chr(c),curses.color_pair(1))
				curr_y,curr_x = stdscr.getyx()
				if index == 0:
					t = time.time()
				index = index +1
				if index > 0:
					cpm = char_counter(t,index)
					cpm = round(cpm,1)
				progress_bar(index,snippet,cpm,y,x,curr_y,curr_x)
				stdscr.refresh()
				break
	return cpm

def progress_bar(index,snippet,cpm,y,x,curr_y,curr_x):
	snippet = len(snippet)
	progress = round(index*30/(snippet))
	stdscr.addstr(y+2,x,"Characters per second : "+str(cpm))
	stdscr.addch(y+3,x,'[')
	stdscr.addch(y+3,x+31,']')
	stdscr.addch(y+3,progress,'=')
	stdscr.move(curr_y,curr_x)


def char_counter(t,index):
	past_time = time.time() - t + 0.1
	chars_per_sec = index/past_time
	return chars_per_sec


def random_snippet(json_string):
	snippet = str(random.choice(json_string))
	return snippet


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


def print_snippet(snippet):
	stdscr.addstr(2,0,str(snippet))
	stdscr.refresh()
	stdscr.addch('\n')
	y,x = stdscr.getyx()
	return y,x

def menu():
	f = Figlet(font = "doom")
	stdscr.addstr(f.renderText("CTRacer"))
	stdscr.addch("\n")
	stdscr.addstr("Choose a language : \n1)Python\n2)C++\n3)Java\n4)PHP\n5)ruby\nPress any other key to exit.")
	input = stdscr.getch()
	match input:
		case 49:
			stdscr.clear()
			return "python"
		case 50:
			stdscr.clear()
			return "cpp"
		case 51:
			stdscr.clear()
			return "java"
		case 52:
			stdscr.clear()
			return "php"
		case 53:
			stdscr.clear()
			return "ruby"
		case other:
			exit()


def main():
	stdscr.clear()
	lang = menu()
	while True:
		stdscr.clear()
		stdscr.addstr("**Press ESC to quite**")
		json_string = open_json(lang)
		snippet = random_snippet(json_string)
		y,x = print_snippet(snippet)
		cpm = typing(snippet,y,x)
		stdscr.clear()
		stdscr.addstr("Your score is : "+str(cpm)+" character per second\n\nPress 'r' to play again\nPress ESC to exit")
		while True:
			restart = stdscr.getch()
			if restart == 114:
				restart = True
				break
			elif restart == 27:
				restart = False
				break
		if not restart:
			break
			

if __name__ == "__main__":
	stdscr = curses.initscr()
	if curses.LINES < 20 or curses.COLS < 40:
		print("Please resize the console to atleast 20 Lines and 40 Colums")
	else:
		curses.start_color()
		main()
