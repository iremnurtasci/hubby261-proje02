from tkinter import *
pencere = Tk()
pencere.title("Yaş-Doğum Tarihi Hesaplama")
pencere.iconbitmap("ico/kitap.ico")
pencere.geometry("550x350")

def HesapYap():
    girilenYas = int(yas.get())
    dogumGoster = 2022 - girilenYas
    sonuc = Label(pencere, text= "Doğum Tarihiniz ya da yaşınız: " + str(dogumGoster))
    sonuc.pack()

baslik = Label(pencere, text= "Yaş-Doğum Hesaplama")
yas = Entry(pencere, width=25, borderwidth=1)
hesapla = Button(pencere, text="Hesapla", command=HesapYap)

baslik.pack()
yas.pack()
hesapla.pack()
#as = int(input("Yaşınızı giriniz: "))
#print(2022 -yas)


pencere.mainloop()