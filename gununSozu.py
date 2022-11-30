from random import choice
from tkinter import *

gununSozleri  = ["Merhaba", "Bu bir örümceğin arayüzüdür :)", "Deneme 1-2-3", "Oldu galiba :))"]
goster = Tk()
#kontrol = 0
def metinGoster():
    #if kontrol == 0:
        gununSecilenSozu = choice(gununSozleri)
        gununSozu = Label(goster, text=gununSecilenSozu)
        gununSozu.pack()
        gununSozu.after(2000, gununSozu.destroy)
        #kontrol = 1
    #else:
        #gununSozu.destroy
        #gununSecilenSozu =choice(gununSozleri)
        #gununSozu = Label(goster, text=gununSecilenSozu)
        #gununSozu.pack()

    #gununSozu.after(2000, gununSozu.destroy)

gununSozuBaslik = Label(goster, text="Günün sözünü görmek için tıklayınız!")
gosterButon = Button(goster, text="Tıkla", command=metinGoster)
gosterKapat = Button(goster, text="Kapat", command=quit)
gununSozuBaslik.pack()
gosterButon.pack()
gosterKapat.pack()


goster.mainloop()

