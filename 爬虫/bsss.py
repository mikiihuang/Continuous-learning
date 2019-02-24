from bs4 import BeautifulSoup
contents = open("soup.txt").read()
a = open("name.txt","a",encoding="utf-8")
# print(contents)
# print(contents)
soup = BeautifulSoup(contents,"html.parser")

dts = soup.find_all("dt",class_="dt mb-4 line")

for item in dts:
    a.write(item.text.strip()+"\n")
