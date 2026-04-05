myList = [1,2,3]
myTuple = (1,2,3)  # degistirilemez

print(type(myList))
print(type(myTuple))


sonuc = myList[0] = 2
sonuc = myTuple[0] = 2 # tuple listte eleman degistirilemez, silinemez veya eklenemez

myList.append(3)
sonuc = myTuple.count(1)

myTuple2 = ([2,3,4]) # listten tuple dondurme
myList2 = ((2,3,4)) # tuple den liste dondurme

print(type(myTuple2))
print(type(myList2))

