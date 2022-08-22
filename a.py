import requests
import time
import bs4
import urllib
import json

def get_list(lang):
	requests.packages.urllib3.disable_warnings() 
	r = requests.get("https://www.codegrepper.com/code-examples/"+lang,verify=False)
	soup = bs4.BeautifulSoup(r.text,'html.parser')
	f = open(lang+'_list.txt','w',encoding='utf-8')

	for ul in soup.select("ul[class='one-third']"):
		for li in ul.find_all("li"):
			f.write(li.get_text()+'\n')
	f.close()

def get_snippet(line):
	s = urllib.parse.quote(line)
	link = "https://www.codegrepper.com/api/get_answers_1.php?v=3&s="+s
	r = requests.get(link,verify=False)
	return r.json()
	
def choose_snippets(lang):
	requests.packages.urllib3.disable_warnings()
	f = open(lang+"_list.txt","r",encoding="utf-8")
	lines = f.readlines()
	snippet_list = []
	for line in lines:
		answer = get_snippet(line)
		if (answer["answers"]):
			answer = answer["answers"][0]["answer"]
			print(answer)
			choice = input("Save the sippet? y/n press f to finish (the json is NOT saved unless you finish): ")
			if choice == "y":
				snippet_list.append(answer)
			if choice == "f":
				save_snippet(lang,snippet_list)
				break
			else:
				pass
			print("#"*50)

def save_snippet(lang,snippets):
	f = open(lang+"_snippets.json","w")
	snippets = json.dumps(snippets,indent=4)
	f.write(snippets)
	f.close()

def read_json():
	f = open("sample.json","r")
	data = json.load(f)
	print(data["samples"][0])

def main():
	lang = input("Choose a language : ")
	#get_list(lang)
	choose_snippets(lang)

if __name__ == "__main__":
	main()	