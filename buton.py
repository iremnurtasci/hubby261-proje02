from tkinter import *

pencere = Tk()

def fonksiyon():
    print("Test")

etiket = Label(pencere, text="Merhaba Dünya")
etiket.pack()

buton = Button(pencere, text="Butona Tıkla!", command=fonksiyon)
buton.pack()

pencere.mainloop()