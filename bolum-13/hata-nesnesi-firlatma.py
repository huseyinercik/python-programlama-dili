# print(10 / 0)

# x = 10
# if x > 5:
#     raise ValueError("x 5 ten buyyuk olamaz")

def renklendir(text, renk):
    renkler = ("blue","red","white","black","orange")
               
    if type(text) is not str : 
        raise TypeError("text str tipinde olmalidir")

    if type(renk) is not str : 
        raise TypeError("text str tipinde olmalidir")

    if renk not in renkler:
        raise ValueError("gecersiz bir renk")
    print(f"{text} {renk} olarak yazildi")


try:
    renklendir("selam", "red")
    renklendir("merhaba", "yellow")
except (TypeError,ValueError) as e:
    print(e)