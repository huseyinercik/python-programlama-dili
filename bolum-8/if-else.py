sonuc = 5 > 3
login = True

if(login):
    print('Merhaba')


email = "emirercik@gmail.com"
parola = "123456"


# login = (email == "emirercik@gmail.com") and (parola == "123456")

# if(login):
#     print("login olundu")
# else:
#     print("email yada parola yanlis")




if(email == "emirercik@gmail.com"):
    if(parola == "123456"):
        print("login olundu")
    else:
        print("parola yanlis") 
else:
    print("email yanlis")


