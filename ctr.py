import requests
from bs4 import BeautifulSoup
import urllib
from easy_getch import getch
import time
import os
import colorama
from colorama import Fore, Back, Style
def test():
	text = "Using this random paragraph generator is very simple.This page generates three random paragraphs by default.You can enter specific words and numbers at the top of the page to generate random paragraphs so that you will get very accurate paragraphs."
	index = 0
	print_text(text)
	for letter in text:
		while True:
			key = getch()
			key = key.decode('ascii')
			if key == letter:
				index = index+1
				print(Fore.GREEN+key,sep=' ',end='',flush=True)
				break
			else:
				pass
			if key == "\x1b":
				break
		if key == "\x1b":
				break
	print("finished")


def key_test():
	key = getch()
	print(key)

def print_text(text):
	print(Fore.WHITE+text)
	print("\n")
	print("#"*100)
	print("\n")
		
def main():
	pass
if __name__ == "__main__":
	colorama.init()
	test()