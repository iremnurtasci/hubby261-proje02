#Grid Sistemi
from tkinter import *

pencere = Tk()
pencere.title("Grid Uygulaması")

baslik = Label(pencere, text="[ Örümceğe Hoş Geldiniz! 🕷️ ]")
etiket1 = Label(pencere, text="[ Örümceği çalıştırmak için butona basınız! ]")
etiket2 = Label(pencere, text="[ Örümceği durdurmak için kapat butonuna basınız! ]")

buton1 = Button(pencere, text="Örümceği Çalıştır", fg="white", bg="black")
buton2 = Button(pencere, text="Kapat", fg="white", bg="black", command=pencere.quit)

baslik.grid(row=0, columnspan=2, padx=50, pady=25)
etiket1.grid(row=1, column=0, padx= 10, pady=10)
etiket2.grid(row=1, column=1, padx= 10, pady=10)

buton1.grid(row=3, column=0, padx=50, pady=25)
buton2.grid(row=3, column=1, padx=50, pady=25)

pencere.mainloop()
