# 1- Bir aracın yakıt tipine göre (benzin, dizel, lpg) belirtilen bir mesafede ne kadar yakıt masrafı olduğunu hesaplayan uygulamayı yapınız.
# benzin : 39.35
# dizel   : 41.71
# lpg     : 20.28

# benzinFiyat = 39.35
# dizelFiyat = 41.71
# lpgFiyat = 20.28
# benzin = "benzin"
# dizel = "dizel"
# lpg = "lpg"

# mesafe = float(input("mesafeyi girin : "))
# yakitTipi = input("Yakit tipini girin : ")

# if(yakitTipi == benzin):
#     print(f"{mesafe} mesafede {benzinFiyat*mesafe} TL benzin masrafiniz olur")
# elif(yakitTipi == dizel):
#     print(f"{mesafe} mesafede {dizelFiyat*mesafe} TL dizel masrafiniz olur")
# elif(yakitTipi == benzin):
#     print(f"{mesafe} mesafede {lpgFiyat*mesafe} TL lpg masrafiniz olur")
# else:
#     print("gecerli bir yakit bilgisi girin")




benzinFiyat = 39.35
dizelFiyat = 41.71
lpgFiyat = 20.28

toplamYakitUcreti = 0
ortalamaYakitTuketimi = float(input("100 km' deki ortalama yakıt tüketimi: "))
gidilecekYol = float(input("Gidilen mesafe: "))
yakitTipi = input("Yakıt Tipi: ")

toplamYakitTuketimi = gidilecekYol * (ortalamaYakitTuketimi / 100)

if(yakitTipi == "benzin"):
    toplamYakitUcreti = benzinFiyat * toplamYakitTuketimi
elif(yakitTipi == "dizel"):
    toplamYakitUcreti = dizelFiyat * toplamYakitTuketimi
elif(yakitTipi == "lpg"):
    toplamYakitUcreti = lpgFiyat * toplamYakitTuketimi
else:
    print("yanlış yakıt tipi")

if(toplamYakitUcreti != 0):
    print(toplamYakitUcreti)

# 2- Bir öğrencinin 2 yazılı bir sözlü notunu alarak ortalama hesaplayınız ve hesaplanan ortalamaya göre not aralığına karşılık gelen değerlendirmeyi yazdırınız.

# 0  -24  => 0
# 25 -44  => 1
# 45 -54  => 2
# 55 -69  => 3
# 70 -84  => 4
# 85 -100 => 5
yaziliNotu1 = int(input("1. yazili notunu girin : "))
yaziliNotu2 = int(input("2. yazili notunu girin : "))
sozluNotu = int(input("sozlu notunu girin : "))
ortalama = (yaziliNotu1 + yaziliNotu2 + sozluNotu) / 3

if(ortalama > -1 and ortalama < 25):
    print(f"Birinci yazili notunuz {yaziliNotu1}, ikinci yazili notunuz {yaziliNotu2}, sozlu notunuz {sozluNotu} oldugundan not ortalamaniz {round(ortalama,2)} cikmistir ve karsiligi 0 'dir")
elif(ortalama > 24 and ortalama < 45):
    print(f"Birinci yazili notunuz {yaziliNotu1}, ikinci yazili notunuz {yaziliNotu2}, sozlu notunuz {sozluNotu} oldugundan not ortalamaniz {round(ortalama,2)} cikmistir ve karsiligi 1 'dir")
if(ortalama > 44 and ortalama < 55):
    print(f"Birinci yazili notunuz {yaziliNotu1}, ikinci yazili notunuz {yaziliNotu2}, sozlu notunuz {sozluNotu} oldugundan not ortalamaniz {round(ortalama,2)} cikmistir ve karsiligi 2 'dir")
if(ortalama > 54 and ortalama < 70):
    print(f"Birinci yazili notunuz {yaziliNotu1}, ikinci yazili notunuz {yaziliNotu2}, sozlu notunuz {sozluNotu} oldugundan not ortalamaniz {round(ortalama,2)} cikmistir ve karsiligi 3 'dir")
if(ortalama > 69 and ortalama < 85):
    print(f"Birinci yazili notunuz {yaziliNotu1}, ikinci yazili notunuz {yaziliNotu2}, sozlu notunuz {sozluNotu} oldugundan not ortalamaniz {round(ortalama,2)} cikmistir ve karsiligi 4 'dir")
if(ortalama > 84 and ortalama < 101):
    print(f"Birinci yazili notunuz {yaziliNotu1}, ikinci yazili notunuz {yaziliNotu2}, sozlu notunuz {sozluNotu} oldugundan not ortalamaniz {round(ortalama,2)} cikmistir ve karsiligi 5 'dir")
else:
    print("Hatali not girildi")