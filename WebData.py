#encoding=utf8
import re
import os
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import urllib2
from bs4 import BeautifulSoup

liste1 = "0123"
os.remove("deneme.txt")
os.remove("siteler.txt")
for i in liste1:
    liste2 = []
    dosya = open("siteler.txt", "a+")
    if int(i) == 0:
        web = "https://www.lyngsat.com/hd/asia.html"
    elif int(i) == 1:
        web = "https://www.lyngsat.com/hd/america.html"
    elif int(i) == 2:
        web = "https://www.lyngsat.com/hd/europe.html"
    elif int(i) == 3:
        web = "https://www.lyngsat.com/hd/atlantic.html"
    page = urllib2.urlopen(web)
    soup = BeautifulSoup(page)


    all_tables = soup.find_all("td", width=180)
    for td in all_tables:
        func = td.find("a").get_text()
        if " " in func:
            func = func.replace(" ", "-")
            func = func.replace("/", "-")
            func = func.replace("'", "")
            func = func.replace("&", "and")
            func = func.replace("ü", "u")
            func = func.replace("ö", "o")
            liste2.append(func)
            dosya.write(func+".html" + "\n")

dosya.close()
with open("siteler.txt", "r") as f:
    data = f.readlines()

for line in data:
    words = line
    web1 = "https://www.lyngsat.com/hd/"+str(words)+""
    page1 = urllib2.urlopen(web1)
    soup1 = BeautifulSoup(page1)
    table = soup1.find("table")
    table_rows = table.find_all("font", {"face": "Verdana"})
    table_rows2 = table.find_all("td", {"colspan": "2"})
    dosya2 = open("deneme.txt", "a+")
    dosya2.write(str(line))
    frequency = []
    sid = []
    for td in table_rows:
        b = td.find_all("b", {"class": ""})
        row = [i.text for i in b]
        if row != []:
            if "V" in i.text:
                frequency.append(str(i.text).replace("V", "\t Vertical \t"))
            elif "H" in i.text:
                frequency.append(str(i.text).replace("H", "\t Horizontal \t"))
            elif "L" in i.text:
                frequency.append(str(i.text).replace("L", "\t Vertical \t"))
            elif "R" in i.text:
                frequency.append(str(i.text).replace("R", "\t Horizontal \t"))
            else:
                frequency.append(str(i.text))
    for td in table_rows2:
        q = re.findall('\d+', td.text)
        for z in q:
            if int(z) > 1000:
                if int(z) < 48000:
                    sid.append(str(z))
                    break
                else:
                    continue
            else:
                continue
    eleman_sayisi = len(sid)
    asda = len(frequency)
    baslangic = 0
    while (baslangic < eleman_sayisi):
        dosya2.write(frequency[baslangic] + sid[baslangic] + "\n")
        baslangic = baslangic + 1
    dosya2.write("\n")
dosya2.close()










