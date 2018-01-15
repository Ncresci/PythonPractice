import requests

from bs4 import BeautifulSoup

base_url = 'http://www.nytimes.com'

r = requests.get(base_url)

soup = BeautifulSoup(r.text)
lines = soup.find_all("h2",{"class": "story-heading"})
open_file = open('nytimes.txt', 'w')

for story_heading in soup.find_all(class_="story-heading"): 
    if story_heading.a: 
        print(story_heading.a.text.replace("\n", " ").strip())
        content = story_heading.a.text.replace("\n", " ").strip()
        open_file.write(content)
    else: 
        print(story_heading.contents[0].strip())
        contents = story_heading.contents[0].strip()
        open_file.write(contents)
        


