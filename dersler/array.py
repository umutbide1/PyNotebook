 
my_list=[1,2,3,4,5]

my_list=["bir",2,True,5.6] # her türlü olur yani

list=["one","two","three"]
list2=["four","five","six"]

number=list[0]+list2[0]

print(number)

print(len(number))

# .split() yazılanı boşluklara ayırarak diziye döndürür

userA=["Umut",22]    #burada göründüğü gibi dizi içine dizi atabiliyoruz
userB=["Ahmet",24]

users=[userA,userB]

print(users)  
print(users[0])  #burada liste içindeki listenin ilki yazılıyor  
print(users[0][0]) # burada da liste içindeki listenin ilk elemanı yazdırılıyor

araclar=["BMW","Mercedes","Opel","Mazda"]

 # liste kaç elemanlıdır 
print(len(araclar))
##############################################


  # kanka burası da listenin ilk ve son elemanını yazdırır
listeninSonElemanininIndisi=len(araclar)-1 
print(araclar[0],araclar[listeninSonElemanininIndisi])
################################################################### 



# mazda ve mercedesin yerini değiştir bakalım 
araclar[1]="Mazda"
araclar[3]="Mercedes"
print(araclar)
########################################################################



# Mercedes Listenin bir elemanı mıdır? kontrol et
aranacakEleman="Mercedes"
dedector=0

for i in range(4):
    if aranacakEleman==araclar[i]:
        print("Eleman bulundu ve ", i ,". indiste yer almakta")
        dedector=dedector+1

if(dedector==0):
    print("Eleman Bulunamadi") 

# Yada şöyle bir çözüm 
sonuc=araclar
sonuc="Mercedes" in araclar 

#############################################################################
    


# dizinin -2 deki indisi nedir ?? dizinin -2 . indisi mi olur ya dedim ama ulan en sondan bakıyormuş vay anasını
print(araclar[-2])

################################################################################

#listenin ilk 3 elemanını alacakmışım 

for i in range(3):
    print(araclar[i])


##############################################################################

#listenin son 2 elamanın yerine Toyota ve Renault yazın 

araclar[-1]="Renault"
araclar[-2]="Toyota"

print(araclar)

#listenin üzerine Audi ve Nissan Markalarını ekleyin

araclar.append("Audi")
araclar.append("Nissan")
print(araclar)

###################################################################################

#listenin son elemanını silelim

araclar.remove(araclar[listeninSonElemanininIndisi-1])
print(araclar)

##################################################################################

#liste elemanlarını tersten yazdiralim

araclar.reverse()
print(araclar)

#########################################################################################
# liste içindeki verileri bir yerde sakla 
bilgiSaklamaListesi=[]
bilgiDegiskeni=""
for i in range(5): # for döngüsü anladım
    bilgiDegiskeni=araclar[i]
    bilgiSaklamaListesi.append(bilgiDegiskeni)


print(araclar)
print(bilgiSaklamaListesi)
############################################################