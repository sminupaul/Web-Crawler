import urllib as lnk

def crawler(link):
    fle = lnk.urlopen(link)
    myFile = fle.read()


    text =""
    link =[]
    sub = "href="
    x = myFile.index('<body',0)

    try:
        while(myFile.index(sub,x)):
            li =[]
            n = (myFile.index(sub, x)+5)
            while(myFile[n] != '>'):
                text += myFile[n]
                n += 1

            li = text.split("\"")
            link.extend(li)

            x = n+1

    except:
        pass

    return link

link=[]
link = crawler(raw_input("Give Any Link To A Website: "))
for i in link:
    print i