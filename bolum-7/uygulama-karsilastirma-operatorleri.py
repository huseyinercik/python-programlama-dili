# 1- Girilen 2 sayıdan hangisi büyüktür?
# sayi1 = int(input("sayi 1 : "))
# sayi2 = int(input("sayi 2 : "))

# sonuc = (sayi1 > sayi2)
# print(f"{sayi1} {sayi2}'den buyuk {sonuc}")
# 2- Girilen bir sayının tek çift kontrolünü yapınız.
# sayi = int(input("sayi : "))
# sonuc = (sayi%2 == 0)
# print(f"{sayi} cift sayi {sonuc}")

# 3- Bir öğrencinin girilen 3 notuna göre başarı durumunu kontrol ediniz. 50 ve üstünde başarılı.

not1 = int(input("not  1 :"))
not2 = int(input("not  2 :"))
not3 = int(input("not  3 :"))

ortalama = (not1 + not2 + not3) / 3
sonuc = (ortalama >= 50)
print(f"Ogrencinin not ortalamasi : {round(ortalama,2)}, basari durumu {sonuc}")
