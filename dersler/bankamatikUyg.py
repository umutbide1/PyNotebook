umutHesap = {
    "ad": "Umut Bide",
    "hesapNo": "564",
    "bakiye": 5000,
    "ekHesap": 2000
}

beyzaHesap = {
    "ad": "Beyzanur Çam",
    "hesapNo": "276",
    "bakiye": 9000,
    "ekHesap": 55000
}

hesaplar = [umutHesap, beyzaHesap]

def paraCek(hesapNumarasi, miktar):
    for hesap in hesaplar:
        if hesap["hesapNo"] == str(hesapNumarasi):
            print("Sayin", hesap["ad"], "Hosgeldiniz.")
            bakiye = hesap["bakiye"]
            ekHesap = hesap["ekHesap"]
            toplamBakiye = bakiye + ekHesap
            if miktar > toplamBakiye:
                print("Hesabinizde yeterli bakiye bulunmamaktadir")
                return False
            else:
                hesap["bakiye"] -= miktar
                print(f"Para cekme isleminiz tamamlandi. Islem sonrasi bakiyeniz: {hesap['bakiye']}")
                return True
    print("Hesap Bulunamadi..")
    return False

paraCek(564, 5500)

#buna eklemeler yapılabilir 
# faiz ekleme bilgisayardan tarih alma gibi bunların hepsini ekleyelim