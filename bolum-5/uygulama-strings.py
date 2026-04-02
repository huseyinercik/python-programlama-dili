title = 'Python ile Programlama Dersleri'

# 1- 'title' degiskeni icerisindeki karakter sayisi nedir?
# 2- 'title' icerisindeki 'Python' kelimesini alin.
# 3- 'title' degiskeninin ilk 5 ve son 5 karakterini alin.
# 4- 'title' degiskenini tersten yazdirin.
# 5- Klavyeden girilen ogrenci bilgisine gore ornek verilen cumleyi yazdiriniz.
#    Ornek : Cinar Turan isimli ogrencinin 1.notu 60, 2. notu 60 ve not ortalamasi 60 olarak hesaplanmistir.

karakterSayisi = len(title)

print(karakterSayisi)

pythonText = title[0:6]

print(pythonText)

ilk5Son5 = title[0:5]+title[-5:karakterSayisi]

print(ilk5Son5)

tersText = title[::-1]

print(tersText)
#    Ornek : Cinar Turan isimli ogrencinin 1.notu 60, 2. notu 60 ve not ortalamasi 60 olarak hesaplanmistir.
ogrenciAd = input("Ogrenci Adi : ")
ogrenciSoyad = input("Ogrenci Soyadi : ")
not1 = input("1. Not : ")
not2 = input("2. Not : ")
notOrtalama = (float(not1) + float(not2) )/ 2

print(ogrenciAd + " " + ogrenciSoyad + " " + "isimli ogrencinin 1. notu" + " " + str(not1) + " " + " 2. notu" + " " + str(not2) + " " + " ve not ortalamasi"
+ " " + str(notOrtalama) + " " + "olarak hesaplanmistir." )

sonuc = f"{ogrenciAd} {ogrenciSoyad} isimli ogrencinin 1.notu {not1}, 2.notu {not2} ve not ortalamasi {notOrtalama} olarak hesaplanmistir."

print(sonuc)