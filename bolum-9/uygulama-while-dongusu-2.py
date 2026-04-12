# Klavyeden girilen n sayıdaki öğrenci bilgisini liste içerisinde saklayınız.
# ** dictionary listesi yapısı (ogrenciNo, ogrenciAdi, ogrenciSoyad) şeklinde olsun.
# ** Ogrenci ekleme işlemi bittiğinde öğrencileri listeleyiniz.

ogrenciler = []
devammi = "e"
# Kullanıcıdan "h" diyene kadar veri alma döngüsü
while (devammi != "h"):
    ogrenciNo = input("öğrenci no: ")
    ogrenciAd = input("öğrenci ad: ")
    ogrenciSoyad = input("öğrenci soyad: ")

    ogrenciler.append({
        "ogrenciNo": ogrenciNo,
        "ogrenciAd": ogrenciAd,
        "ogrenciSoyad": ogrenciSoyad,
    })
    devammi = input("devam mı? (e/h): ")

# Kayıtlı öğrencileri listeleme
for ogrenci in ogrenciler:
    print(f"{ogrenci['ogrenciNo']} numaralı öğrencinin adı {ogrenci['ogrenciAd']} {ogrenci['ogrenciSoyad']}")