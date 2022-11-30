from tkinter import *
from PIL import ImageTk, Image

pencere = Tk()
pencere.title("Sabahattin Ali'nin Kitapları")
pencere.iconbitmap("ico/kitap.ico")
pencere.geometry("750x650")

gorsel = ImageTk.PhotoImage(Image.open("img/kitap_01.jpg"))

def fotoTutucu():
    gorselTutucu = Label(image=gorsel)
    gorselTutucu.pack()


butonum=Button(pencere, text="Foto Göster", command=fotoTutucu)
butonum.pack()

pencere.mainloop()