programlama_diller = ["Python", "C#", "Java", "Javascript"]

sonuc = programlama_diller # ['Python', 'C#', 'Java', 'Javascript']
sonuc = type(programlama_diller) # 'list'
sonuc = programlama_diller[0:2] # ['Python', 'C#']
sonuc = programlama_diller[:2] # ['Python', 'C#']
sonuc = programlama_diller[0:] # ['Python', 'C#', 'Java', 'Javascript']
sonuc = programlama_diller[-3:-1] # ['C#', 'Java']
sonuc = programlama_diller[-3:] # ['C#', 'Java', 'Javascript']


# Guncelleme
programlama_diller[-1] = "Php" # ['Python', 'C#', 'Java', 'Php']
 
sonuc = programlama_diller
sonuc = len(programlama_diller) # 4
sonuc = programlama_diller + ["Go", "Delphi"] # ['Python', 'C#', 'Java', 'Php', 'Go', 'Delphi']

sonuc = "Python" in programlama_diller # True
sonuc = "React" in programlama_diller # False   # Kosul ifadeleri

del programlama_diller[0] # ['C#', 'Java', 'Php']

for i in programlama_diller:
    print(i)

