# Kalıtım konusu önemli bu 
# person class ı düşün tepede bu class olacak ve diğer classlar buradan miras alacak

#tekrar tekrar özellik yazmaktansa yukarıdakileri direkt geçirmek çok daha manalı yani 

class Person:
    def __init__(self) -> None:
        print("Kisi olusturuldu.")
    def whoAmI(self):
        print("I am i person")
          
class Student(Person):
    def __init__(self) -> None:
        super().__init__()
       # Person.__init__(self)
        print("Ogrenci olusturuldu.")

person1=Person()
student1=Student()
# İnhertance biraz karısık bir daha bakılabilir
print(person1.whoAmI()) 
print(student1.whoAmI()) #student kalıtım aldığı için fonksiyona bu da erişebiliyor 

# ezme işlemleri biraz sıkıntılı 
# override kısmına bir bakılabilir 
# 8.4 kısım 4. yer kalılnan  




    