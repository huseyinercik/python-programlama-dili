def selamlama(isim):
    return "Merhaba, " + isim

# print(selamlama("Emir"))
# print(selamlama("Nefise"))

def toplama(sayi1, sayi2):
    return sayi1 + sayi2

# print(toplama(10,20))
# print(toplama(10,30))


def yasHesapla(dogumYili):
    return 2026 - dogumYili

def emekliligeKacYilKaldi(dogumYili,isim):
    yas = yasHesapla(dogumYili)

    kalanSure = 65 - yas

    if kalanSure > 0 :
        return f"{isim}, emekliliginize {kalanSure} yil kaldi"
    else: 
        return f"{isim}, zaten {abs(kalanSure)} yil once emekli oldunuz" 

print(emekliligeKacYilKaldi(1983, "Huseyin"))
print(emekliligeKacYilKaldi(1984, "Nefise"))
print(emekliligeKacYilKaldi(2014, "Emir"))
print(emekliligeKacYilKaldi(1950, "Mehmet"))



