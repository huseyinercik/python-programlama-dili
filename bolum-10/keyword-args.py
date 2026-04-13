def fullName(fisrtName : str, lastName : str, age : int =30) -> str:
    return f"Your name is {fisrtName} {lastName} {age}"

sonuc = fullName("Emir", "Ercik")
sonuc = fullName(lastName="Ercik",fisrtName= "Emir")
sonuc = fullName(lastName="Ercik",fisrtName= "Emir")
sonuc = fullName(fisrtName="Emir",lastName="Ercik",age=12)


print(sonuc)