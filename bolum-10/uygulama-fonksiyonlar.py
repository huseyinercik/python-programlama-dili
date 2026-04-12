# 1- Kendisine gönderilen bir kelimeyi belirtilen kez ekranda gösteren fonksiyon.
def yazdirma(kelime, tekrar):
    return kelime * tekrar

print(yazdirma("Merhaba ", 5))

# 2- Dikdörtgenin alan ve çevresini hesaplayan fonksiyon.

def hesapla(kisa, uzun):
    alan = kisa * uzun
    cevre = 2 * (kisa + uzun)
    return f"alan {alan}, cevre {cevre}"

sonuc = hesapla(10,20)
sonuc = hesapla(20,30)



# 3- Yazı tura uygulamasını fonksiyon kullanarak yapınız. (Random modülü)

def yaziTura():
    import random
    sayi = random.random()

    if sayi > 0.5:
        return "Tura"
    else:
        return "Yazi"
    
sonuc = yaziTura()

print(sonuc)


# 4- Kendisine gönderilen 2 sayı arasındaki tüm asal sayıları bulan fonksiyon.

def asalSayilariBul(sayi1, sayi2):
    for i in range(sayi1, sayi2+1):
        if(sayi1 > 1):
            for x in range(2, i):
                if(i % x == 0):
                    break
            else:
                print(i)

asalSayilariBul(10,20)


# 5- Bir sayının tam bölenlerini liste şeklinde döndüren fonksiyon.

def tamBolenleriBul(sayi):
    tamBolenler = []

    for i in range(2, sayi):
        if(sayi % i == 0):
            tamBolenler.append(i)
    return tamBolenler

print(tamBolenleriBul(20))
