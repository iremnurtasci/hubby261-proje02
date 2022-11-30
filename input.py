from tkinter import *

pencere = Tk()

def fonksiyon():
    etiket = Label(pencere, text="Merhaba Örümceğe Hoş Geldiniz! " + metin.get())
    etiket.pack()


metin = Entry(pencere, width=25, borderwidth=5)
metin.insert(0, "Varsayılan metin!")
metin.pack()

buton = Button(pencere, text="Butona Tıkla!", command=fonksiyon)
buton.pack()

pencere.mainloop()