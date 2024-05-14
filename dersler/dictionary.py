#key value

sehirler=["Kocaeli","Istanbul"]
plakalar=[41,34]

print(plakalar[sehirler.index("Kocaeli")])

print(plakalar[sehirler.index("Istanbul")])

#bunlar dictionary olmadan 

plakalar={"Kocaeli":41,"Istanbul":34}
print(plakalar["Kocaeli"])

# plakalar["Ankara"]=6 # bu da yenisini ekliyor bu key wordslere 

# print(plakalar)

users = {
    "UmutBide":22,    # buralarda aslında umutbide şeklinde dizinin indisi ekrana yazdırılmak istendiğinde bir yada birden fazla yere götürmesi
    "AhmetBurhan":21,       # istenebilir bu gibi durumlarda bu yapıyı kullanmalıyız.Mesela bir users dizisi içinde bir key ve word eşlemesi yaptık
    "YilmazSoke":45,        # bu eşlemeden sonra biz aşağıdaki gibi ekrana çıktı almak istediğimizde bu key bizi yanında ki bütün değerlere götürür
    "MustafaColak":56       # mesela bir insanın adını girerek her türlü bilgisine ulaşılmak istendiğinde bu yapı gayet mantıklı aslında 
    }
print(users["AhmetBurhan"])

#  #şimdi daha manalı ve daha sağlam bir yapı kuruyoruz kanka 

userss={"Bahtiyar":{
        "age":22,
        "mail":"bahtiyar@gmail.com",
        "adress":"Sivas"
        },
        "Bahadir":{
            "age":24,
            "mail":"bahadir@gmail.com",
            "adress":"Ordu"
        },
        "Umut":{
        "age":21,
        "mail":"umut@gmail.com",
        "adress":"Kocaeli"
        },
        }

print(userss["Umut"])
print(userss["Umut"]["age"]) #ikinci kısım spesifik bir istek 

#sevdim burayı baya yararlı duruyor açıkçası

#iki tane uygulama yapıcaz birincisinde yukarıdaki yapıyı kendimiz buradan oluşturmayacağız da tek tek dışarıdan konsoldan alacağız.
#ikinci uygulamada ise dışarıdan bir bilgi alacağız ve o bilgiye denk gelen keyword bilgilerini ekrana çıkaracağız.Mesela id gibi

ogrenciler={}

number=input("Ogrenci No: ")
name=input("Ogrenci Adi: ")
lastName=input("Ogrenci Soyadi: ")
phone=input("Ogrenci Telefon: ")

ogrenciler[number]= {
    "ad":name,
    "soyad":lastName,
    "Telefon":phone
}

print(ogrenciler)

# bu yapı biraz karışık ama kullanışlı sorun yok
