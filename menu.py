from tkinter import *
from tkinter import ttk
from urllib.parse import urlparse
import urllib.request
from bs4 import BeautifulSoup
import os

pencere = Tk()
pencere.title("Ana Menü")
pencere.geometry("380x280")

def urllistele():
    pencere1 = Tk()
    pencere1.title("URL LİSTESİ")
    pencere1.geometry("500x350")
    with open("dataURL.txt") as f:
        liste = f.read()
    etiket = Label(pencere1, text=liste)
    etiket.pack()
    buton1 = Button(pencere1, text="Geri Dön", command=pencere1.destroy)
    buton1.pack()


def urlekle():
    pencere2 = Tk()
    pencere2.title("URL EKLE")
    pencere2.geometry("500x350")
    urlGir = Entry(pencere2)
    urlGir.pack()
    buton2 = Button(pencere2, text="URL Ekle", command=lambda:dosyaEkle(urlGir.get()))
    buton2.pack()
    def dosyaEkle(url):
        URLkontrol = urlparse(url)
        if URLkontrol == "http://" or "https://":
            with open("dataURL.txt", "a") as f:
                f.write(url + "\n")
                print("URL eklendi!")
        else:
            print("URL hatalı!")
            urlGir.pack()
        pencere2.destroy()


def orumcekgonder():
    pencere3 = Tk()
    pencere3.title("ÖRÜMCEK GÖNDER")
    pencere3.geometry("500x350")


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
    print("Örümcek gönderildi.")
    buton3 = Button(pencere3, text="Geri Dön", command=pencere3.destroy)
    buton3.pack()

def sonuclarilistele():

    pencere4 = Tk()
    pencere4.title("SONUÇLAR")
    pencere4.geometry("500x350")
    with open("getURL.txt") as f:
        liste = f.read()
    etiket = Label(pencere4, text=liste)
    etiket.pack()
    buton4 = Button(pencere4, text="Geri Dön", command=pencere4.destroy)
    buton4.pack()

def cikis():
    pencere5 = Tk()
    pencere5.title("ÇIKIŞ")
    pencere5.geometry("500x350")
    buton5 = Button(pencere5, text="Çıkış Yap", command=quit)
    buton5.pack()


menuElemanlari = ["URL Listele", "URL Ekle", "Örümcek Gönder", "Sonuçları Listele", "Çıkış Yap"]
menuFonksiyonlari = [urllistele, urlekle, orumcekgonder, sonuclarilistele, quit]

for idx, eleman in enumerate(menuElemanlari):
    ttk.Button(pencere, text="" + eleman, command=menuFonksiyonlari[idx]).pack()


pencere.mainloop()
