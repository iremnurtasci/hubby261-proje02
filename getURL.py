import urllib.request
from bs4 import BeautifulSoup
import os


class GetURL:
    dataFile = "dataURL.txt"
    getFile = "getURL.txt"

    def __init__(self):
        fileTest = open(self.getFile, 'a')
        fileTest.close()

    def getWeb(self):
        
        print("Örümcek çalışıyor...🕷️")

        dataOpen = open(self.dataFile, 'r')
        getOpen = open(self.getFile, 'w')

        for dataGet in dataOpen:
            webSite = urllib.request.urlopen(dataGet)
            getBytes = webSite.read()
            webPage = getBytes.decode("utf8")
            soup = BeautifulSoup(webPage, 'html.parser')
            getOpen.write(("\n" + dataGet.strip() + " - " + soup.title.contents[0] + "\n" + soup.select_one("p").text))
            print(soup.get_text())
            webSite.close()
        dataOpen.close()
        getOpen.close()

        print("Çalışma tamamlandı!")

    def getList(self):
        getOpen = open(self.getFile, 'r')
        if os.stat("getURL.txt").st_size == 0:
            print("Henüz ziyaret edilmiş adres yok!")
        else:
            print("Ziyaret edilmiş adresler var!")
        for dataShow in getOpen:
            print(dataShow)
        getOpen.close()
