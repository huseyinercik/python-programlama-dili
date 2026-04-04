# 1- "Toyota, Bmw, Renault, Mercedes" elemanlarına sahip markalar isimli bir liste oluşturunuz.
otomobiller = ["Toyota", "Bmw", "Renault", "Mercedes"]
# 2- Liste kaç elemanlıdır?
sonuc = len(otomobiller)
print(sonuc)
# 3- Listenin ilk ve son elemanı nedir?
sonuc = otomobiller[0]
print(sonuc)
sonuc = otomobiller[-1]

# 4- "Renault" markasını "Togg" ile güncelleyiniz.
sonuc = otomobiller[-2] = "Togg"
print(otomobiller)
# 5- "Togg" listenin bir elemanı mıdır?
sonuc = "Togg" in otomobiller
print(sonuc)
sonuc = "Togg" not in otomobiller
print(sonuc)

# 6- Listenin ilk 2 elemanını alınız.
sonuc = otomobiller[:3]
print(sonuc)
# 7- Listenin sonuna "Ford" ve "Citroen" markalarını ekleyiniz.
sonuc = otomobiller + ["Ford", "Citroen"]
print(sonuc)
# 8- Listenin son elemanını siliniz.
del otomobiller[-1]
print(otomobiller)
# 9- Aşağıdaki verileri liste içerisinde saklayınız.

    # öğrenci1: Yiğit Bilgi 2010 [70,80,90]
    # öğrenci2: Ada Bilgi   2011 [70,70,80]
    # öğrenci3: Çınar Turan 2017 [60,60,90]
ogrenci1 = ["Yiğit","Bilgi",2010,[70,80,90]]
ogrenci2 = ["Ada","Bilgi",2012,[70,70,80]]
ogrenci3 = ["Çınar","Turan",2017,[60,60,90]]

ogrenciler = [ogrenci1,ogrenci2,ogrenci3]

# 10- Öğrencilerin yaşlarını hesaplayınız.
# yasYigit = 2024 - ogrenci1[2]
# yasAda = 2024 - ogrenci2[2]
# yasCinar = 2024 - ogrenci3[2]

yasYigit = 2024 - ogrenciler[0][2]
yasAda = 2024 - ogrenciler[1][2]
yasCinar = 2024 - ogrenciler[2][2]

print(yasYigit, yasAda, yasCinar)

# 11- Öğrencilerin not ortalamalarını hesaplayınız.

notYigit = (ogrenciler[0][3][0] + ogrenciler[0][3][1] + ogrenciler[0][3][2]) / 3
notAda = (ogrenciler[1][3][0] + ogrenciler[1][3][1] + ogrenciler[1][3][2]) / 3
notCinar = (ogrenciler[2][3][0] + ogrenciler[2][3][1] + ogrenciler[2][3][2]) / 3


print(notYigit, notAda, notCinar)