#import file
from bs4 import BeautifulSoup
#import lxml

with open("website.html") as file:
    contents =  file.read()
soup = BeautifulSoup(contents,"html.parser")
# print(soup.title)
# print(soup.title.string)

#print(soup.prettify())
all_anchore_tags = soup.find_all(name="a")
#print(all_anchore_tags)

# for tag in all_anchore_tags:
#     print(tag.getText)
#     print(tag.get("href"))

heading = soup.find(name="h1",id="name")
# print(heading)

section_heading = soup.find(name="h3",class_="heading")
print(section_heading)

h3_heading = soup.find_all("h3",class_ = "heading")
print(h3_heading)

# from bs4 import BeautifulSoup