# ASAL SAYI YALNIZ KENDİSİNE VE 1  E BÖLÜNEN SAYI
# 1 E HEPSİ BÖLÜNÜR ZATEN KENDİSİNE DE HEPSİ BÖLÜNÜR O ZAMAN KENDİSİ İLE 1 ARASINDA SAYILARA BÖLÜNÜYOR MU ONA BAKICAZ 
while True:
    sayi=int(input("bir sayi giriniz asal mi kontrol edelim: "))
    if sayi==1:
        print("Asal degildir")
        exit()
    sayiKontrol=sayi-1
    sayiKontrolDizisi=[]
    while sayiKontrol>1:
        eklenecekSayi=sayi%sayiKontrol
        sayiKontrolDizisi.append(int(eklenecekSayi))
        sayiKontrol=sayiKontrol-1

    for x in sayiKontrolDizisi:
        if x==0:
            print("Asal Degildir")
            break
    else:
        print("Asaldir")
# Yapı anlaşıldı 