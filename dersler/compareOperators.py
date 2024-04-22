
import sys
# klasik karsilastirma islemleri

# SORU   GİRİLEN İKİ SAYIDAN HANGİSİ BUYUKTUR?

x=int(input("Birinci degeri giriniz: "))
y=int(input("Ikinci degeri giriniz: "))

if(x>y):
    print("Birinci girilen sayinin degeri daha buyuktur.")
elif(y>x):
    print("İkinci deger birinci degerden daha buyuktur.")
else:
    print("sayilar esittir")

#KULLANICIDAN 2 VİZE (%60) VE FİNAL NOTU (%40) NOTUNU ALIP ORTALAMA HESAPLAYINIZ

vizeNotu=int(input("Vize notunuzu giriniz: "))
finalNotu=int(input("Final notunuzu giriniz: "))

ortalama=float((vizeNotu*60)+(finalNotu*40))/100

print("Not ortalamaniz: ", ortalama)
if(ortalama>=50):
    print("Tebrikler,gectiniz")
elif(ortalama<50):
    print("Uzgunuz,kaldiniz")    
# GİRİLEN SAYİNİN TEK Mİ ÇİFT Mİ OLDUĞUNU KONTROL EDEN YAZILIM

q=int(input("Lutfen bir sayi giriniz: "))

if(q%2==0):
    print("Sayi cifttir.")
else:
    print("Sayi tektir.")

# GİRİLEN SAYININ BİR NEGATİF BİR POZİTİF DURUMUNU YAZDIRIN 

sayi=int(input("Kontrol edilecek sayiyi giriniz: "))

if sayi>0:
    print("Sayi pozitiftir")
elif sayi==0:
    print("Sayinin pozitif negatiflik durumu mevcut degil")

else:
    print("Sayi negatiftir")
#PAROLA VE EMAİL BİLGİSİNİ İSTEYİP DOĞRULUĞUNU TESPİT EDELİM
print("KAYIT EKRANINA HOSGELDINIZ")

email=str(input("E-mail adresinizi giriniz: "))
sifre=str(input("Olusturmak istenen sifrenizi giriniz: "))
sifreKontrol=str(input("Sifrenizi tekrar giriniz: "))
if sifre!=sifreKontrol:
    print("Sifreler eslesmiyor..")
    sys.exit()
elif sifre==sifreKontrol:
    print("Girilen bilgiler icin tesekkurler")

print("GİRİS EKRANINA HOSGELDINIZ")
girisEmail=str(input("Lutfen E-mail giriniz: "))
girisSifre=str(input("Lutfen sifrenizi giriniz: "))
if (girisEmail==email and girisSifre==sifre):
    print("Hosgeldiniz..")
else:
    print("Dolandirmaya calismaa")

























