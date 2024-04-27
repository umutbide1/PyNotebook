x="global"

def function():
    x="local"

function()
print(x)

#fonksiyon içinde olanlar fonksiyonlar için özel bir çalışma alanı oluşturur global olanı değiştirmez.
# dinamik statik kapsam bağlama konusu Muhammed Fatih Adak hocamız anlatıp sormuştu.

name="Umut"

def changeName(newName):
    name=newName
    print(name)

changeName("Pide") # fonksiyon içinde tanımlanan iş böyle
print(name) #burada iş globale dönüyor


