a, b, c = 4, 8, (12, 2)

# 1- Kullanıcıdan aldığınız 2 sayının çarpımı ile a,b,c toplamının farkı nedir?
kullaniciSayi1 = int(input("1. sayiyi girin : "))
kullaniciSayi2 = int(input("2. sayiyi girin : "))
kullaniciSayiCarpimi = kullaniciSayi1*kullaniciSayi2
# c1 = c[0]
# c2 = c[1]
# abcToplam = a + b + c1 + c2
abcToplam = a + b + c[0] + c[1]
sonuc = kullaniciSayiCarpimi - abcToplam
print(sonuc)

# 2- c' nin b' ye kalansız bölümünü hesaplayınız.
# c = c1 + c2
# sonuc1 = c // b
sonuc1 = (c[0] + c[1]) // b
print(sonuc1)
# 3- (a,b,c) toplamının mod 7' si nedir?
sonuc2 = abcToplam % 7
print(sonuc2)

# 4- b' nin a. kuvvetini hesaplayınız.
sonuc3 = b ** a
print(sonuc3)
# 5- a, *b, c = (2,4,6,8,13) işlemine göre c' nin küpü nedir?
a, *b, c = (2,4,6,8,13) # c = 13 oluyor yani a = 2, c = 13, kalan sayilar yildiz kullanimindan dolayi b = [4,6,8]
print(c ** 3)


# 6- a, b, *c = (2,4,6,8,13) işlemine göre c' nin değerleri toplamı nedir?
a, b, *c = (2,4,6,8,13)
print(c[0]+c[1]+c[2])