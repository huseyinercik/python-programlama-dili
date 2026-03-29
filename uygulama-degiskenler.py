"""
Asagidaki musterinin bilgilerini ve sayin aldigi urun bilgilerini degiskenler icerisine saklayiniz
Toplam odenen ucret nedir?
Odenen miktarin kdv orani nedir? (%18)

Sadik Turan
05321234567
info@sadikturan.com
Kocaeli

Satin Alinan Urunler

Urun Adi : Kablosuz Mouse
Fiyati : 550 TL

Urun Adi : Kablosuz Klavye
Fiyati : 650 TL

Urun Adi : Dizustu Bilgisayar
Fiyati : 55.000 TL
"""

musteriAdi = "Sadik"
musteriSoyadi = "Turan"
musteriGSM = "05321234567"
musteriEMail = "info@sadikturan.com"
musteriAdres = "Kocaeli"
urun1 = "Kablosuz Mouse"
urun1Fiyat = 550
urun2 = "Kablosuz Klavye"
urun2Fiyat = 650
urun3 = "Dizustu Bilgisayar"
urun3Fiyat = 55000

toplamUcret = urun1Fiyat+urun2Fiyat+urun3Fiyat

print("Toplam Ucret : "+ str(toplamUcret) )

kdv = 0.18
odenenKDVOrani = toplamUcret*kdv
print("Odenen KDV Orani : "+ str(odenenKDVOrani))

# str(100) => "100" + "Ali" => 100Ali
