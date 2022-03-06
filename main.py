import requests
import bs4


#globals
description = []
authorName = []
bookName= []
f = open('text.txt', 'a')


def main():
    res = requests.get('https://nostarch.com')
    res.raise_for_status()



    noStarchSoup = bs4.BeautifulSoup(res.text, 'html.parser')
    scrape(noStarchSoup)


def scrape(noStarchSoup):
    name = noStarchSoup.select('div.field-name-field-author')
    descript = noStarchSoup.select(' div.field-type-text-with-summary ')
    elems = noStarchSoup.select('article')
    printing(name,descript,elems)


def printing(name,descript,elems):

    for i in range(len(elems)):
        word=elems[i].getText()
        title=(word.split('\n'))
        bookName.append(title[2])



    for i in range(len(name)):
        #print(name[i].getText())
        authorName.append(name[i].getText())
        #print(str(elems[i]))
        #print(name[i].getText())


    for i in range(len(descript)):
        description.append(descript[i].getText())


    for j in range(len(description)):
        line = "Author: ", authorName[j] , ", Book name: ", bookName[j] , ",Summary: ", description[j]
        f.writelines(line)

    f.close()




main()