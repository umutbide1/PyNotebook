# KORKMA ACI BÜYÜTÜR İNSANI, SON KEZ OLSUN SALLA ZARLARI GÜÇLÜ OL YORULMADAN SADECE YÜRÜ,ARKANA BAKMA
from datetime import datetime
import time
#İF ELSE KOŞUL BLOKLARI İLE ÖRNEKLER 

# SORU   KULLANICIDASN İSİM YAŞ EĞİTİM BİLGİLERİ İSTENİP EHLİYET ALIP ALAMAMA DURUMU KONTROL EDİLECEK.
# EHLİYET ALMA ŞARTLARI EN AZ 18 YAŞINDA VE EĞİTİM DURUMU LİSE YA DA ÜNİVERSİTELİ OLMALIDIR.
#ÇOK FARKLI ŞEKİLLERDE YAPILABİLİR FAKAT BEN BOOL İLE YAPMAK İSTİYORUM 

isim=str(input("Isminiz nedir: "))
cinsiyet=str(input("Cinsiyetiniz nedir: (erkek/kadin)"))
if cinsiyet=="kadin":
    cinsiyet="hanim"
elif cinsiyet=="erkek":
    cinsiyet="bey"
yas=int(input("Yasiniz nedir: "))
egitimDurumu=str(input("Egitim durumunuz lise veya lisans seviyesinde mi?:evet/hayir "))

ehliyetAlabilir=False

if yas>18 and yas<60 and egitimDurumu=="evet":
    ehliyetAlabilir=True
else:
    ehliyetAlabilir=False

if ehliyetAlabilir==True:
    print(isim,cinsiyet,",ehliyet alabilirsiniz harc biraz yuksek ama :)")
else:
    print(isim,cinsiyet,",ne yazik ki bilgileriniz ehliyet almaya müsait degil")

#SORU BİR ÖĞRENCİNİN 2 YAZILI 1 TANE SÖZLÜ SINAVI VARDIR BU NOTLARI ONDAN AL HESAPLANAN NOTA GÖRE ONA 0 5 ARASINDA BİR DEĞER BİÇ
#HEPSİ AYNI AĞIRLIKTA SINAVLARIN KOLAYLIK OLSUN İSTERSEN YAZILILAR 35 35 30 ŞEKİLNDE ALABİLİRİZ 

yazili1=int(input("Ilk sinav notunuzu giriniz: "))
yazili2=int(input("Ikinci sinav notunuzu giriniz: "))
sozlu=int(input("Sozlu notunuzu giriniz: "))

genelNot=((sozlu*30)/100)+((yazili1*35)/100)+((yazili2*35)/100)
print("Genel ortalamaniz: ",genelNot)
if  0<=genelNot<=24:
    print("Notunuz: 0 ")
elif 25<=genelNot<=44:
    print("Notunuz: 1")
elif 45<=genelNot<=54:
    print("Notunuz: 2")
elif 55<=genelNot<=69:
    print("Notunuz: 3")
elif 70<=genelNot<=84:
    print("Notunuz: 4")
elif 85<=genelNot<=100:
    print("Notunuz: 5")

#TRAFİĞE ÇIKIŞ TARİHİNİ ALINAN BİR ARACIN SERVİS ZAMANINI AŞAĞIDAKİ GİBİ HESAPLA
# İLK BAKIM 1. SENE İKİNCİ BAKIM 2. SENE 3. BAKIM 3. SENE YAPILACAK ŞEKİLDE OLACAKMIŞ DATELİNE MODÜLÜ LAZIM
# while True:
#     bugun = datetime.today()
#     print(bugun)
#     time.sleep(1)
bugun = datetime.today()

print("Sisteme hosgeldiniz,Aracinizin trafige cikis tarihiyle alakali bilgileri sizden rica edecegiz")
gun = int(input("Günü giriniz: "))
if gun>31:
    print("hatali gün bilgisi girdiniz..")
    exit()
ay = int(input("Ayi giriniz: "))
if ay>12:
    print("hatali ay bilgisi girdiniz..")
    exit()
yil = int(input("Yili giriniz: "))
if yil>bugun.year:
    print("hatali yil bilgisi girdiniz..")
    exit()
girilenTarih = datetime(yil, ay, gun)

gecenGunSayisi = (bugun - girilenTarih).days

gecenYilSayisi=int(gecenGunSayisi/360)

print("Arac trafige ciktigi sureden itibaren ",gecenYilSayisi," yil gecmistir.")



