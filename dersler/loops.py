# # dizileri gezmek için ideal mesela 

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45] 
 
for num in numbers: # liste adedi kadar döner ne yazdıracağımız bize kalmış ama anlamadığım şey illa bir bir mi artıyor?
    print(num)


names=["Umut","Beyzanur"]
for name in names:
    print("My name is",name)    # daha ilkel bir kullanım 
    print(f"my name is {name}") # daha modern bir kullanım 

name="Umut Bide"

for n in name:
    print(n)  #char dizisinde her bir eleman kendi başına bir eleman gibi değerlendirildiğinden harfleri ekrana tek tek yazar 

sayilar= [1,3,5,7,9,12,19,21]
tekSayilarDizisi=[]
# # SAYILARDAN HANGİLERİ 3 UN KATIDIR 

sayac=0
for sayi in sayilar:
    if (sayi%3==0):
        print(f"{sayi} sayisi 3 ün bir katidir.Diziye eklendi")
        tekSayilarDizisi.append(sayi)

for tekSayi in tekSayilarDizisi:
    print(f"Ucun katlari olan sayilar su sekildedir: {tekSayilarDizisi}")

# # SAYILARIN TOPLAMI
sayilarToplam=0
for sayilarToplami in sayilar:
    sayilarToplam=sayilarToplami+sayilarToplam

print(f"sayilarToplam: {sayilarToplam}")


# # SAYILARIN İÇERİSİNDEKİ TEK SAYILARIN KARELERİNİ AL VE EKRANA BASTIR
eklenecekSayi=0
tekSayilarKareDizi=[]
for tekSayilar in sayilar:
    if tekSayilar%2==1:
        eklenecekSayi=tekSayilar**2
        tekSayilarKareDizi.append(eklenecekSayi)  # Lenght ile de yapılabilir ama ben tercih etmedim.
    
print(f"Tek sayilar sunlardir: {tekSayilarKareDizi}")



sehirler=["Kocaeli","Istanbul","Ankara","Izmir","Rize"]

#ŞEHİRLERİN HANGİLERİ EN FAZLA 5 KARAKTERLİDİR? 
sehirHarfiSayaci=0
for sehir in sehirler:
    for charSehir in sehir:
        sehirHarfiSayaci=sehirHarfiSayaci+1
        #print(charSehir)
    if sehirHarfiSayaci <= 5:
        print(sehir)
    sehirHarfiSayaci=0

# ################################ WHİLE DONGUSU KONUSU 

# 1 den 100 e kadar sayıları tanımla ve ekrana yaz mesela bunu while ile yapmak daha mantıklı 

x=0
# koşul tamamlanana kadar true koşul tamamlandığında false döner ve döngü kırılır

# while True:
#     print(x) # bu sonsuz bir döngü mesela o yüzden koşulu kendi insifyatifimizde düzgün seçmeliyiz.

while x<=100:
    print(x)
    x+=1
print("Bitti gitti geçmis olsun")


name =""
while not name or name=="abdulmuttalip":  # bak mesela burada name değeri boş bir değer veya abdulmuttalip :) değeri ise 
    name=input("Isim giriniz :")          # tekrar değer girilmesini istiyor yani gerçek bir uygulamada kullanılabilr gayet mantıklı bir yapı 
print(f"Hosgeldin {name}")


#WHİLE İLE İLGİLİ ÖRNEK UYGULAMALAR
sayilar1= [1,3,5,7,9,12,19,21]
# SAYİLAR LİSTESİNİ WHİLE İLE EKRANA BASTIRALIM 
sayac=int(0) 
while sayac<=len(sayilar1):
    print(sayilar1[sayac],end=" ")
    sayac=sayac+1


#BAŞLANGIC VE BİTİS DEGERLERİNİ ALIP ARADAKİ BUTUN TEK SAYILARI YAZDIRAN PROGRAM WHİLE İLE 
while True:
    baslangicDegeri=int(input("Lutfen baslangic degerini giriniz: "))
    bitisDegeri=int(input("Luften bitis degerini giriiniz: "))
    if baslangicDegeri >= bitisDegeri:
        print("Girmis oldugunuz deger araliklari iki aralik arasindaki tek sayilari bulma islemine uygun degildir..Tekrar deneyiniz.")
    elif baslangicDegeri < bitisDegeri:
        break
while True:
    if baslangicDegeri%2==1 and baslangicDegeri<=bitisDegeri: 
        baslangicDegeri=baslangicDegeri+2
        if baslangicDegeri < bitisDegeri:
            print(baslangicDegeri)
        if baslangicDegeri >=bitisDegeri:
            break
    else:
        baslangicDegeri=baslangicDegeri+1
    
# 0 VE 100 ARASINDAKİ SAYILARİ AZALAN BİCİMDE YAZDİRİN WHİLE İLE
yuz=0
sifirYuzArasiDizi=[]
while yuz<=100:
    sifirYuzArasiDizi.append(yuz)
    yuz=yuz+1
yuz=yuz-1  
while yuz>=0:
    print(sifirYuzArasiDizi[yuz], end=" ")
    yuz=yuz-1

#KULLANİCİDAN ALACAGINIZ 5 SAYİYİ SIRALİ BİR SEKİLDE YAZDİRİNİZ.

alinacakSayiAdedi=int(input("kac adet sayi ile islem yapacaginizi belirleyiniz: "))
siralanacakDizi=[]
sayac=1
while alinacakSayiAdedi>0:
    alinacakSayiAdedi=alinacakSayiAdedi-1
    x=int(input(f"{sayac}. sayiyi giriniz: "))
    sayac=sayac+1
    siralanacakDizi.append(x)
siraliDizi=sorted(siralanacakDizi)

print(f"Siralanmis diziniz su sekildedir {siraliDizi}")










