urunler = [
    {"urunAdi": "Hp Victus", "fiyat": 32999},
    {"urunAdi": "Lenovo ThinkPad", "fiyat": 25499},
    {"urunAdi": "Apple Macbook", "fiyat": 49999},
    {"urunAdi": "Huawei Matebook", "fiyat": 26999},
    {"urunAdi": "Casper Nirvana", "fiyat": 20000},
    {"urunAdi": "Hp Victus", "fiyat": 32999}

]

# 1- Aşağıdaki örnek cümleyi tüm ürünlere uygulayınız:
#    "Hp Victus marka ürünün fiyatı 32999 Türk Lirası."
# for i in urunler:
#     print(f"{i['urunAdi']} marka ürünün fiyatı {i['fiyat']} Türk Lirası.")


# 2- Ürünlerin fiyatları toplamı nedir?
# toplam = 0
# for i in urunler:
#     toplam += i["fiyat"]
# print(toplam)

# 3- 25000 ile 40000 arasındaki ürünleri listeleyiniz.
# for i in urunler:
#     if i["fiyat"] > 24999 and i["fiyat"] < 40001 :
#         print(i["urunAdi"])

# 4- Kullanıcıdan alınan anahtar kelimeye göre ürünleri listeleyiniz.
secim = input("marka girin : ")
for i in urunler : 
    if (i['urunAdi'].lower().find(secim.lower()) > -1):
        print(i["urunAdi"])