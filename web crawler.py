import requests
from bs4 import BeautifulSoup



def trade_spider():


        url = "http://localhost/_mylab/"
        source_code = requests.get(url)
        # just get the code, no headers or anything
        plain_text = source_code.text
       # print(plain_text)
        # BeautifulSoup objects can be sorted through easy
        soup = BeautifulSoup(plain_text,'html.parser')
        for link in soup.findAll('a'):
            href = "http://localhost/_mylab/" + link.get('href')
            title = link.string  # just the text, not the HTML
            print(title)
            print(href)
            get_single_item_data(href)

def get_single_item_data(item_url):
    source_code = requests.get(item_url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text,'html.parser')
    # if you want to gather links for a web crawler
    for link in soup.findAll('a'):
        href = "http://localhost/_mylab/" + link.get('href')
        title = link.string
        print(title)
        print(href)
def get_admin_content():
    url = "http://localhost/_mylab/nwlab/admin.php"
    source_code = requests.get(url)
    plain_text = source_code.text
   # print plain_text
    soup = BeautifulSoup(plain_text,'html.parser')
    for link in soup.findAll('a'):
        href = "http://localhost/_mylab/nwlab/" + link.get('href')
        title = link.string
        print(title)
        print(href)
get_admin_content()
#trade_spider()