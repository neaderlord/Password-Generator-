import os
import random
import tkinter as tk
from tkinter import *
import customtkinter
import string
import pyperclip
from tkinter import messagebox

# Ekran
ekran = tk.Tk()
ekran.geometry("500x200")
ekran.title("Şifre Oluşturucu")

# Şifre Üretme
def cryp(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    outlbl.configure(text=password)

# Kopyalama Komutu
def kopyala():
    kopy = outlbl.cget("text")
    pyperclip.copy(kopy)
    if kopy == "":
        messagebox.showerror(title="Hata!", message="Lütfen Şifre Üretin")
    else:
        messagebox.showinfo(title="Başarılı!", message="Başarılı Şekilde Kopyalandı")

# Kaydetme Komutu
def kayıt():
    kayt = outlbl.cget("text")  # Şifreyi al
    if not kayt:
        messagebox.showerror(title="Hata!", message="Lütfen Şifre Üretin")
    else:
        ekran2 = tk.Tk()
        ekran2.geometry("300x150")
        ekran2.title("Dosya Adı Girin")

        # Kaydet butonu
        def kayıd():
            dosya = kaytentry.get()  # Dosya adını al
            dosya_yolu = os.path.join("passwords", dosya)  # "passwords" klasörünün içine kaydetmek için dosya yolu
            with open(dosya_yolu, 'w') as file:
                file.write(kayt)
            messagebox.showinfo(title="Başarılı!", message="Başarılı Şekilde Kaydedildi")
            ekran2.destroy()

        kaytbuton = Button(master=ekran2, text="Kaydet", command=kayıd)
        kaytbuton.pack(side=BOTTOM, pady=20)

        # Text Box
        kaytentry = tk.Entry(master=ekran2, width=20)
        kaytentry.pack(pady=30)

        mainloop()

# Klasörü kontrol et ve oluştur
if not os.path.exists("passwords"):
    os.makedirs("passwords")

# Butonlar
buton = customtkinter.CTkButton(master=ekran, text="Kaydet", anchor="n", width=250, height=30, command=kayıt)
buton.pack(side=BOTTOM, pady=10)
buton1 = customtkinter.CTkButton(master=ekran, text="Kopyala", anchor="n", width=250, height=30, command=kopyala)
buton1.pack(side=BOTTOM)
buton1 = customtkinter.CTkButton(master=ekran, text="Üret", anchor="n", width=250, height=30, command=cryp)
buton1.pack(side=BOTTOM, pady=10)

# Output Yazısı
outlbl = Label(ekran, text="", width=38, height=8)
outlbl.pack()

tk.mainloop()
