# Dictionary metotlari

yemekTarifi = {
    "yemekAdi" : "Musakka",
    "yemekTarifi" : "Tarif Aciklamasi",
    "resim" : "1.jpeg"
}

# acces items
sonuc = yemekTarifi["yemekAdi"] # Musakka
sonuc = yemekTarifi.get("yemekAdi") # Musakka
sonuc = yemekTarifi.keys()
sonuc = yemekTarifi.values()
sonuc = yemekTarifi.items()

# update items
# yemekTarifi["yemekAdi"] = "Manti" # dict_items([('yemekAdi', 'Manti'), ('yemekTarifi', 'Tarif Aciklamasi'), ('resim', '1.jpeg')])
# yemekTarifi.update({"yemekAdi" : "Manti"}) # dict_items([('yemekAdi', 'Manti'), ('yemekTarifi', 'Tarif Aciklamasi'), ('resim', '1.jpeg')])
# yemekTarifi.update({"yemekAdi2" : "Manti"}) #dict_items([('yemekAdi', 'Manti'), ('yemekTarifi', 'Tarif Aciklamasi'), ('resim', '1.jpeg'), ('yemekAdi2', 'Manti')])

# delete items
# yemekTarifi.pop("yemekAdi") # dict_items([('yemekTarifi', 'Tarif Aciklamasi'), ('resim', '1.jpeg')])
# yemekTarifi.popitem() # dict_items([('yemekAdi', 'Musakka'), ('yemekTarifi', 'Tarif Aciklamasi')])
yemekTarifi.clear() # dict_items([])

# copy => referans
print(sonuc)