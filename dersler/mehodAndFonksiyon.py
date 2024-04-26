#Method python da kendi içerisinde olan kullanılabilir fonksiyonlar ama bunlar hazır yazılmış yani .append() gibi .pop gibi 
#import ediyoruz ve daha sonrasında içerisinden rahatça kullanabiliyoruz bu methodlara 
#Fonksiyonu ise biz şimdi ellerimizle yazıcaz daha emekli olacaktır.
#python un kendi sitesinde bu methodları tek tek bulabilir ve neler yapılabilir onu anlayabiliz.Bakmak çok mantıklı aslında.
#Classları biz de yazıcaz aslında kütüphaneler classlardan olusuyor ve bu kütüphaneyi de kendimiz yazıcaz yani 

#def fonksiyonAdi 
 
# def sayHello(name="Kullanici adi belirtilmedi"):  # parametre yollanmazsa default bunu yazar yani
#     return f"Merhaba ilk fonksiyon yazan kisi de: {name}"
# msgg=sayHello()
# print(msgg)



# def total(num1,num2):
#     return num1+num2
# donenDeger=total(5,7) #genel mantık açık örnekleri bekliyorum 
# print(donenDeger)

# PARAMETRELER 

# def changeName(n):
#     n="umut"

# def changeCity(sehirler):   #DİZİLERDE ADRES GÖNDERİLİR ONDAN DEĞİSTİRİLİR AMA DİREKT BİR İNT YA DA STRİNG DE BU BOYLE DEGİL BU BİR REFERANS
#     sehirler[0]="istanbul"

# sehir=["Ordu","Bilecik"]

# changeCity(sehir)

# print(sehir)

# def topla(*parameters):   # istediğin kadar parametre ver hocam mod on galiba referanslar sayesinde yapıyor bunu 
#     return sum((parameters))


# def kullaniciBilgileri(**parameters):
#     for key,value in parameters.items():
#         print("{} is {}".format(key,value))

# kullaniciBilgileri(name= "Umut", age=21, city="Ordu")
# kullaniciBilgileri(name= "Beyza", age=22, city="Bilecik", number="276")
# kullaniciBilgileri(name= "Seda", age=23, city="Canakkale", number="296", email="seda@gmail.com")

# tuple listesi verilmek isteniyorsa fonksiyona tek * eğer dictionary şeklinde yollamak istersem ** kullanıcam 


def myFunc(a,b,*args,**kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)

myFunc(10,20,30,40,50,60,70, key1="value1",key2="value2")















