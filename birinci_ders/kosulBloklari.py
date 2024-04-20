# if else yapılarını biraz daha yakından tanımak adına alıştırma
username="umutbide"
password="umut123"
isLoggedin=False
kullaniciAdi=input("Kullanici Adinizi giriniz: ")
kullaniciParola=input("Kullanici Adinizi giriniz: ")
if kullaniciAdi==username and kullaniciParola==password: 
    isLoggedin=True

if isLoggedin==True:
    print("Hosgeldiniz")
else:
    isLoggedin==False
    print("Tanisiyor muyuz?")


