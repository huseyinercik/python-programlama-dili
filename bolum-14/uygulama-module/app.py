# module1 (db)      : urunler
# module2 (methods) : urunEkle(), urunGuncelle(), urunleriGetir()
# module3 (app)     :

# yeni ürün ekleme => urunEkle("iphone 15", 60000)
# ürün güncelle    => urunGuncelle(1, "iphone 15 pro", 80000)
# ürünleri listele => urunleriGetir()

from method import *
sonuc = urunleriGetir()

urunEkle("Iphone 20",90000)
urunEkle("samsung s20",90000)


for i in urunleriGetir():
    print(i["urunAdi"])


urunGuncelle(1, "iphone 15 Pro",80000)
# for i in sonuc:
#     print(i["urunAdi"])

for i in urunleriGetir():
    print(i["urunAdi"])
