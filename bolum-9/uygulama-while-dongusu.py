# 1- Başlangıç ve bitiş değerlerini kullanıcıdan alınız ve bu değerler arasındaki tüm çift sayıları yazdırınız.

# baslangic = int(input('Baslangic sayisi girin : '))
# bitis = int(input('Bitis sayisi girin : '))

# while (baslangic < bitis):
#     if baslangic %2 == 0 :
#         print(baslangic)
#     baslangic +=1


# 2- (1-100) arasındaki sayıları azalan şekilde yazdırınız.

# baslangic = 0
# bitis = 100

# while (bitis > baslangic):
#     print(bitis)
#     bitis -= 1


# 3- Kullanıcıdan alacağınız 5 sayıyı ekranda sıralı bir şekilde yazdırın.
# giris = 0
# sayilar = []
# while giris < 5 :
#     sayi = int(input('sayi girin : '))
#     sayilar.append(sayi)
#     giris += 1

# sayilar.sort()
# print(sayilar)


# 4- Klavyeden girişi istenen username bilgisi için boşluk girildiği sürece tekrar username girişi isteyiniz.

username = ""

while not username:
    username = input('kullanici adi : ')

print("Girilen Username : " +username)


