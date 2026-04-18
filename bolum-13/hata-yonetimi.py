while True:
    try:
        x = int(input("x : "))
        y = int(input("y : "))
        print(x / y)
    except (ZeroDivisionError, ValueError) as e: 
        print("x ve y sayi olmalidir. sifir olamaz.")
    except Exception as e:
        print("bilinmeyen bir hata olustu")
        print(e)
    else:
        break
    finally:
        print("finally blogu calisti.")
