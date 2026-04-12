# isim = "Emir Ercik"

# for i in isim :
#     if(i == 'E'):
#         break
#     print(i)




i = 0
toplam = 0
while (i < 101):
    i += 1
    if(i %2 == 1):
        continue
    toplam += i
    
print(toplam)