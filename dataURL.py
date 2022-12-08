import os
class DataURL:

  dataFile = "dataURL.txt"

  def __init__(self):
    fileTest = open(self.dataFile, 'a')
    fileTest.close()

  def dataWrite(self):
    dataOpen = open(self.dataFile, 'a')
    siteURL = input("Site adresini ön eki ile birlikte giriniz: ")
    kontrolHTTP = siteURL[:7]
    kontrolHTTPS = siteURL[:8]
    if kontrolHTTP == "http://" or kontrolHTTPS == "https://":
      print("URL Doğru! Web Sitesi Eklendi.")
      dataOpen.write(siteURL + "\n")
    else:
      print("URL Hatalı! Lütfen yeniden giriniz. (http:// ya da https:// olmalı)")
      siteURL = input("Site adresini ön eki ile birlikte giriniz: ")
      print("URL Doğru! Web Sitesi Eklendi.")
      dataOpen.write(siteURL + "\n")

    dataOpen.close()

  def dataRead(self):
    dataOpen = open(self.dataFile, 'r')
    if os.stat("dataURL.txt").st_size == 0:
      print("Dosya BOŞ!")
    else:
      print("Dosya DOLU!")
    for dataShow in dataOpen:
      print(dataShow)
    dataOpen.close()