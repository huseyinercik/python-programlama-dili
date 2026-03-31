"""
Uygulama 1 : Yari capi verilen bir dairenin alan ve cevresini hesaplayiniz
Alan : πr²
Cevre : 2πr

Uygulama 2 : Klavyeden girilen km bilgisini mil cinsinden hesaplayiniz
mil = km / 1.609344
"""

# r = float(input("Dairenin yari capini girin : "))
# π = 3.14
# alan = π*(r**2) # alan = π*r*r
# cevre = 2*π*r
 
# print("Dairenin alani : "+str(alan))
# print("Dairenin cevresi : "+str(cevre))

km = float(input("Km bilgisini girin : "))
oran = 1.609344
mil = km / oran
mil = round(mil,2)

print("Girilen km : "+ str (mil) +" mil'dir")
