from tkinter import *
import subprocess

def word():
    degiskenler = ent1.get()
    min_char = ent2.get()  # 'min' isimli değişken kullanımı tavsiye edilmez, gömülü fonksiyon ismi ile çakışabilir
    max_char = ent3.get()
    try:
        subprocess.run(["crunch", min_char, max_char, degiskenler, "-o", "you_wordlist.txt"], capture_output=True, text=True, check=True)
        print("Wordlist başarıyla oluşturuldu.")
    except subprocess.CalledProcessError as e:
        print(f"Hata: {e}")

pencere1 = Tk()

pencere1.geometry("500x300+300+0")
pencere1.title("Wordlist Yapıcı")

label2 = Label(pencere1, text="Lütfen wordlist karakterlerini giriniz (karakterler arasına ',' koymayınız):")
label2.pack()
ent1 = Entry(pencere1, width=50)
ent1.pack()

lab3 = Label(pencere1, text="Minimum karakter uzunluğunu giriniz:")
lab3.pack()
ent2 = Entry(pencere1, width=10)
ent2.pack()

lab4 = Label(pencere1, text="Maksimum karakter uzunluğunu giriniz:")
lab4.pack()
ent3 = Entry(pencere1, width=10)
ent3.pack()

label1 = Label(pencere1, text="Wordlist oluşturmak için tıkla:")
label1.pack()

buton = Button(pencere1, text="Tıkla", command=word)
buton.pack()

pencere1.mainloop()
