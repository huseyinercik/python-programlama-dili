# 1- Yaşı 18' den büyük ya da veli izni varsa bir işte çalışabilir durumunu kontrol ediniz.
# yas = int(input("yas : "))
# izin = int(input("izin : "))
# sonuc = (yas > 18) or (True == 1)
# print(f"calisabilme durumu {sonuc}")


# 2- Ders notu 50-100 arasındaysa geçti değilse kalsın bilgisini yazdırınız.
# notBilgisi = int(input('not :'))
# sonuc = (notBilgisi > 50) and (notBilgisi < 100)
# print(f"Ders gecme durumu {sonuc}")

# 3- Not ortalaması en az 70 puan ve zayıfı yoksa teşekkür belgesi alabilme durumunu kontrol ediniz.
# notOrtalamasi = int(input("Not ortalamasi : "))
# zayif = int(input("Zayif : "))
# sonuc = (notOrtalamasi >= 70) and not(zayif == True)
# print(f"Tesekkur Belgesi alma durumu {sonuc}") 


# 4- İşe girmek için en az önlisans ya da lisans mezunu olma durumunu kontrol ediniz. Sigara kullanmama koşulu.
# mezuniyet = input("Mezuniyet : ")
# sigaraKullanimi = int(input("Sigara kullaniyor mu : "))
# sonuc = ("onlisans" == mezuniyet or "lisans" == mezuniyet) and (not(sigaraKullanimi == True))
# print(f"Ise girebilme durumu {sonuc}") 

# 5- Uygulamaya giriş kontrolünü "username yada email" ve "parola" için yapalım.
kullaniciBilgi = input("Kullanici bilgisi : ")
kullaniciParola = input("Parola : ")
sonuc = (kullaniciBilgi == "username" or kullaniciBilgi == "email") and (kullaniciParola == "parola")
print(f"Uygulamaya login olabilme durumu {sonuc}")

