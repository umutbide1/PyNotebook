# Modülden kasıt kütüphaneler
#
#
#
# Kendi yazdığımız kütüphaneler
# Hazır Modüller (Numpy,Pandas) gibi 
#   a-)Standart Kütüphane modülleri
#   b-)Üçüncü şahış Modüller

# pypi.org     Kütüphanelerin işlevlerini ve fonskiyonlarını tanıtan harika bir site

import math as islem # burada mesela kütüphaneye kendim isim verdim 

# value= dir(islem)
# value=help(islem)
# print(value)


from math import * # burada mesela math kütüphanesinden bütün modülleri çekiyor ayrı ayrı da çekebiliyormuşuz
import random
from math import sqrt,factorial # parça parça import muhabbeti
#3. videoda kaldık

#rastgele sayı üretmek için bir deneme yapılıyor şuan o yüzden buraları hızlı geçiyorum
names=["Umut","Beyza"]
result = random.choice(names) #listenin içerisinden rastgele bir elemanı seçen modül

# random kütüphanesinin metotları kısaca ufak bir araştırma ile de bulunabilir 

liste = list(range(10))
random.shuffle(liste) # burada liste her defasında karışık bir şekide ekrana basılacak daha doğrusu belledeğe alınacak harika bence 
print(result)
print(liste)