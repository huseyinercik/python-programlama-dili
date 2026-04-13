def selamlama(isim = "Kullanici", mesaj = "Iyi gunler"):
    return f"{isim} {mesaj}"

sonuc = selamlama("Emir", "Merhaba")
sonuc = selamlama("Ali", "selam")
sonuc = selamlama("Emir")

def usAlma(taban, us = 2):
    return taban ** us

sonuc = usAlma(2,3)
sonuc = usAlma(5)

print(sonuc)


def toplam(a, b):
    return a+b

def cikarma(a,b):
    return a-b

def islem(a, b, fn = toplam):
    return fn(a,b)

sonuc = islem(10, 20 , cikarma)
sonuc = islem(10, 20)
sonuc = islem(10, 20 , toplam)


print(sonuc)