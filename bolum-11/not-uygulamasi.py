# Not Uygulaması

# 1- Menu
    # 1- Not Gir
    # 2- Ortalamaları Göster (90-100 -> AA, 85-89 -> BA)
    # 3- Notları Kayıt Et
    # 4- Çıkış

# 90-100 -> AA
# 80-89  -> BA
# 75-89  -> BB
# 70-74  -> CB
# 65-69  -> CC
# 60-64  -> DC
# 50-59  -> DD
# 40-49  -> FD
# 0 - 39 -> FF

def notHesapla(satir):
    satir = satir[:-1]
    liste = satir.split(":")

    ogrencininAdi = liste[0]
    notlar = liste[1].split(",")

    not1 = int(notlar[0])
    not2 = int(notlar[1])
    not3 = int(notlar[2])

    ortalama = (not1 + not2 + not3) / 3

    if ortalama > 89 and ortalama < 101:
        harf = "AA"
    elif ortalama > 79 and ortalama < 90:
        harf = "BA"
    elif ortalama > 74 and ortalama < 80:
        harf = "BB"
    elif ortalama > 69 and ortalama < 75:
        harf = "CB"
    elif ortalama > 64 and ortalama < 70:
        harf = "CC"
    elif ortalama > 59 and ortalama < 65:
        harf = "DC"
    elif ortalama > 49 and ortalama < 60:
        harf = "DD"
    elif ortalama > 39 and ortalama < 50:
        harf = "FD"
    elif ortalama > 0 and ortalama < 40:
        harf = "FF"

    return f"{ogrencininAdi} : {harf} - ({ortalama})\n"

def notGir():
    ad = input("Ogrenci adi : ")
    soyad = input("Ogrenci soyad : ")
    not1 = input("Not 1 : ")
    not2 = input("Not 2 : ")
    not3 = input("Not 3 : ")
    with open("sinavNotlari.txt","a",encoding="utf-8")as file:
        file.write(ad + ' ' + soyad + ':' + not1 + ',' + not2 + ',' + not3 + '\n')

def notlariOku():
    with open("sinavNotlari.txt","r",encoding="utf-8")as file:
        for satir in file:
            print(notHesapla(satir))

def notlariKaydet():
    with open("sinavNotlari.txt","r",encoding="utf-8")as file:
        liste = []

        for satir in file:
            liste.append(notHesapla(satir))

    with open("sonuclar.txt","w",encoding="utf-8")as file2:  
        file2.writelines(liste)

while True:
    islem = input("1- Not Gir\n2- Notlari Oku\n3- Notlari Kayit Et\n4- Cikis\nsecim : ")

    if islem == "1":
        notGir()
    elif islem == "2":
        notlariOku()
    elif islem == "3":
        notlariKaydet()
    else:
        break