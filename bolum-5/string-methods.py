mesaj = "bTK akademi, python kursu "

# sonuc = mesaj.upper() BTK AKADEMI PYTHON KURSU
# sonuc = mesaj.lower() btk akademi python kursu
# sonuc = mesaj.title() Btk Akademi Python Kursu
# sonuc = mesaj.capitalize() Btk akademi python kursu

# sonuc = "abc".isupper() False
# sonuc = "abc".islower() True

# sonuc = mesaj.strip() " BTK Akademi Python Kursu " => "BTK Akademi Python Kursu" bosluklari aliyor
# sonuc = mesaj.split() ['BTK', 'Akademi', 'Python', 'Kursu'] 
# sonuc = mesaj.split(',') " BTK Akademi, Python Kursu " => [' BTK Akademi', ' Python Kursu '] virgulden ayirir

# sonuc = mesaj.index("akademi") 5
# sonuc = mesaj.startswith("a") False
# sonuc = mesaj.endswith("u") True

# sonuc = mesaj.replace("python","java") bTK akademi, java kursu
# print (sonuc)