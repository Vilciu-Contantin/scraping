from bs4 import BeautifulSoup

with open("website.html") as fp:
    soup = BeautifulSoup(fp, "html.parser")

for paragraph in soup.find_all("h1"):
    print(paragraph.text)
