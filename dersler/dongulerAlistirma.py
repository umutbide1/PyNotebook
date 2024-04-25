# ORNEKLER*************
# 1 100 ARASINDA RASTGELE SAYİ URETILECEK BİR SAYIYI ASAGI YUKARI İFADELERİ İLE BULDURMAYA CALISIN
## HER YARDIM 20 PUAN AZALMAYA SEBEP OLACAK 
## KAC ADET DENEME HAKKIMIZ VAR ONU KULLANICIDAN ALIN VE ONA GORE CAN HAKKINIZ OLSUN 
## ASLINDA SÖYLE YAPSAK DAHA İYİ MESELA 100 PUAN YA KAÇ HAK OLURSA 100 Ü ONA BOLELİM VE HER KALAN HAKKI ÇARPI O HAK ADEDİ KADAR PUAN ALSIN
### BU OYUNDA ZATEN EN FAZLA 7 TAHMİNDE BİLEBİLİYORUZ O ZAMAN KAÇ ADET TAHMİN İSTİYOR ONA GÖRE ADAMA AVANS VERELİM
import random 
import time
# while True:
#     sayi=random.randrange(0,100)
#     print(sayi)
#     time.sleep(0.1)           # RASTGELELİK BU ŞEKİLDE SAĞLANACAK


print("SAYI TAHMİN UYGULAMASINA HOŞGELDİNİZ.")
print("0 100 ARASINDAN MAKİNEMİZİN RASTGELE URETTİGİ SAYIYI KENDI ARZU ETTIGINIZ TAHMIN ADEDI KADAR DENEYEREK BULMAYA CALISACAKSINIZ.")
print("PUANLANDIRMA GIRMIS OLDUGUNUZ TAHMININ KACINCISINDA BULDUGUNUZA GORE DEGISECEKTIR.")
print("SAYI TAHMİN UYGULAMASINA HOŞGELDİNİZ.")

sayi=random.randrange(0,100)
donguAdediSayaci=0
tahminSayaci=0
kacAdetTahmin=int(input("Kac adet tahmin yapmak istersiniz?: "))
puan=100
i=0
while i < kacAdetTahmin:
    i=i+1
    tahminSayaci=tahminSayaci+1
    donguAdediSayaci=donguAdediSayaci+1
    x=int(input(f"Tahmin olusturulan sayiyi tahmin etmeye calisiniz({tahminSayaci}.tahmininiz): ")) 
    if sayi<x:
        print("Girmis oldugunuz sayi olusturulan sayidan buyuktur.Daha asagida bir tahmin yapiniz.")
        puan=puan-int(100/kacAdetTahmin)
    elif sayi>x :
        print("Girmis oldugunuz sayi olusturulan sayidan kucuktur.Lutfen daha yukarida bir tahmin yapiniz.")
        puan=puan-int(100/kacAdetTahmin)
    elif sayi==x:
        print(f"Tebrik ederiz.Sayiyi dogru tahmin ettiniz...Puaniniz: {puan}") 
        break
    if kacAdetTahmin==donguAdediSayaci:
        print("Uzgunuz tahmin hakkiniz bitti ve dogru cevabi bulamadiniz..")
        print("SAYI" , sayi , "di. Bİ DAHA OYNAMA SEN!")
        break
    #deneme    github proj değişim denenme anlamaya calisma