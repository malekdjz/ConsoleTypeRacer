import curses
import json
import random
import time
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
					stdscr.addstr(y+2,x,"Characters per second : "+str(cpm))
					stdscr.move(curr_y,curr_x)
				stdscr.refresh()
				break
	return cpm


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
	try:
		stdscr.addstr(2,0,str(snippet))
		stdscr.refresh()
	except:
		print("The console needs to be bigger")
		quit()
	stdscr.addch('\n')
	y,x = stdscr.getyx()
	return y,x

def menu():
	stdscr.addstr("Choose a language : \n1)Python\n2)C++\n3)Java\n4)PHP\nPress any other key to exit.")
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
		stdscr.addstr("Your score is : "+str(cpm)+" character per second\n\nPress 'r' to play again\nPress any key to exit")
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
	curses.start_color()
	main()
