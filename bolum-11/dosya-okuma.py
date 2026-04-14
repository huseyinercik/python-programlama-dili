'''
Dosya açmak ve oluşturmak için open() fonksiyonu kullanılır.

Kullanımı : open(dosya_adi, dosya_erişme_modu)
dosya_erişme_modu : dosyayı hangi amaçla açtığımızı belirtir.
"r" okuma modu : okuma modu. belirtilen konumda dosya olmalıdır.
seek : cursor konumu
'''

f = open("log.txt", encoding='utf-8') # dosyayi aciyor

print(f.read())
print(f.read())

f.read() # bastan satiri okuyor
f.read() # tekrar yazildiginda cursorun altindaki satira geciyor
f.seek(0) # cursoru en ust 1. satira cekiyor
f.readline() # cursor satir satir okur
f.readlines() # Tum satirlari liste halinde gelir
f.closed # dosya acikmi diye kontrol eder
f.close() #  dosyayi kapatir
# kapatilan dosya islem yapmak icin yine open metodu ile acmak gerek
