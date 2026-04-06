"""
Sets
İndekslenemez (Elemanlara [0] gibi indekslerle ulaşılamaz)

Sıralanamaz (Elemanlar bellek üzerinde belirli bir sırada tutulmaz)

Güncellenemez (Var olan bir elemanın değeri doğrudan değiştirilemez)

Elemanlar tekrarlanamaz (Her eleman küme içerisinde sadece bir kez bulunabilir)

Eleman siler ya da ekleriz (Kümenin içeriği yeni eleman ekleyerek veya mevcut olanı silerek değiştirilebilir)
"""
meyveler = {"elma","armut","kiraz","elma"} # {'kiraz', 'elma', 'armut'}
meyveler2 = {"elma","armut","kiraz","kavun"} # {'kiraz', 'elma', 'armut'}

# sonuc = meyveler[0]


sonuc = meyveler



for i in meyveler:
    print(i)

sonuc = "elma" in meyveler # True

meyveler.add("karpuz") # ekleme
meyveler.update(meyveler2) # iki set listi birlestirir uniqe olarak gosterir tum elemanlari
# meyveler.remove("visne") # raise an error siler eleman yoksa hata firlatir
meyveler.discard("armut") # siler eleman yoksa hata firlatmaz
meyveler.pop() # rastgele siler
meyveler.clear() # tumunu siler
print(sonuc)

