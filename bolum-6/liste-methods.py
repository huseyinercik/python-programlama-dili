sayilar = [4,6,8,2,56,78,90]
isimler = ['ahmet','canan','zeynep','gokhan','canan']

sonuc = min(sayilar) # 2
print(sonuc)
sonuc = min(isimler) # ahmet
print(sonuc)
sonuc = max(isimler) # zeynep
print(sonuc)
sonuc = max(sayilar) # 90
print(sonuc)

# ekleme
sayilar.append(12) # [4, 6, 8, 2, 56, 78, 90, 12]
print(sayilar)
isimler.append('cinar') # ['ahmet', 'canan', 'zeynep', 'gokhan', 'canan', 'cinar']
print(isimler)

sayilar.insert(0,100) # [100, 4, 6, 8, 2, 56, 78, 90, 12]
print(sayilar)
sayilar.insert(-1,100) # [100, 4, 6, 8, 2, 56, 78, 90, 100, 12]
print(sayilar)
sayilar.insert(-3,100) # [100, 4, 6, 8, 2, 56, 78, 100, 90, 100, 12]
print(sayilar)
sayilar.insert(len(sayilar),100) # [100, 4, 6, 8, 2, 56, 78, 100, 90, 100, 12, 100]
print(sayilar)

# silme
sayilar.pop() # [100, 4, 6, 8, 2, 56, 78, 100, 90, 100, 12]
print(sayilar)
sayilar.pop(0) # [4, 6, 8, 2, 56, 78, 100, 90, 100, 12]
print(sayilar)

isimler.remove('zeynep') # ['ahmet', 'canan', 'gokhan', 'canan', 'cinar']
print(isimler)

# siralama 
sayilar.sort() # [2, 4, 6, 8, 12, 56, 78, 90, 100, 100]
print(sayilar)
isimler.sort() # ['ahmet', 'canan', 'canan', 'cinar', 'gokhan']
print(isimler)

# tersten siralama
sayilar.reverse() # [100, 100, 90, 78, 56, 12, 8, 6, 4, 2]
print(sayilar)
isimler.reverse() # ['gokhan', 'cinar', 'canan', 'canan', 'ahmet']
print(isimler)

# sayma

sonuc = sayilar.count(4) # 1
print(sonuc)

sonuc = isimler.count('canan') # 2

print(sonuc)

sonuc = sayilar.index(4)
print(sonuc)

















