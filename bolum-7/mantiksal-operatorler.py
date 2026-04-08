# (yas >= 18)  =>true, false
# (mezuniyet == 'lise') ya da (mezuniyet == 'universite') =>true, false
# sonuc = (yas >= 18) ve (mezuniyet == 'lise') ve ya (mezuniyet == 'universite')

x = 11

sonuc = (x > 5) and (x < 10)
# 1- And (Ve)
#   True, True   => True
#   True, False  => False
#   False, False => False

# 2- Or (Veya)
#   True, True   => True
#   True, False  => True
#   False, False => False

sonuc = (x > 0) and (x % 2 == 0)    # x pozitif çift sayı
sonuc = (x > 0) or (x % 2 == 0)     # x pozitif ya da çift sayı

# 3- Not
# False => True
# True => False
sonuc = not(x > 0)

print(sonuc)

