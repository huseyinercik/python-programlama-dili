# Bankamatik Uygulaması

# Hesap bilgileri tutulacak. (dict)
# menu, paraCekme, bakiyeSorgula, paraYatirma fonksiyonları tanımlanacak.
# çekilmek istenen tutar hesapta yoksa ek hesabın kullanılmak istendiği sorulacak.


hesaplar = [
    {
        "ad":"Sadik Turan",
        "hesapNo":"12345",
        "bakiye":20000,
        "ekHesap":5000,
        "username":"sadikturan",
        "password":"1234"
    },
    {
        "ad":"Efe Turan",
        "hesapNo":"12345",
        "bakiye":30000,
        "ekHesap":10000,
        "username":"efeturan",
        "password":"1234"
    }
]

def menu(hesap):
    print("\n")

    print(f"merhaba, {hesap["ad"]}")

    print("1- Bakiye Sorgulama")
    print("2- Para Cekme")
    print("3- Para Yatirma")

    islem = input("Yapmak Istediginiz Islem : ")

    if islem == "1":
        bakiyeSorgula(hesap)
    elif islem == "2":
        paraCekme(hesap)
    elif islem == "3":
        paraYatirma(hesap)
    else:
        print("hatali secim")

    menu(hesap)

def bakiyeSorgula(hesap):
    print(f"bakiye : {hesap["bakiye"]}")
    print(f"ek bakiye : {hesap["ekHesap"]}")


def paraCekme(hesap):
    miktar = float(input("cekmek istediginiz miktar : "))
    if hesap["bakiye"] >= miktar:
        hesap ["bakiye"] -= miktar
        print("paranizi alabilirsiniz")
    else:
        toplam = hesap["bakiye"]+hesap["ekHesap"]

        if toplam >= miktar:
            ekHesapKullanimIzni = input("ek hesap kullanilsin mi? (e/h)")

            if ekHesapKullanimIzni == "e":
                kullanilacakMiktar = miktar - hesap["bakiye"]
                hesap["bakiye"] = 0
                hesap["ekHesap"] -= kullanilacakMiktar
                print("paranizi alabilirsiniz")
            else:
                print("hesabiniz yetersiz")
        else:
            print("hesabiniz yetersiz")

def paraYatirma(hesap):
    pass

def login():
    username = input("username : ")
    password = input("password : ")

    isLoggedIn = False

    for hesap in hesaplar:
        if hesap["username"]==username and hesap["password"]==password:
            isLoggedIn = True
            menu(hesap)
            break
    if not(isLoggedIn):
        print("username yada password hatali...")

login()