# # Kalıtım konusu önemli bu 
# # person class ı düşün tepede bu class olacak ve diğer classlar buradan miras alacak

# #tekrar tekrar özellik yazmaktansa yukarıdakileri direkt geçirmek çok daha manalı yani 

# class Person:
#     def __init__(self) -> None:
#         print("Kisi olusturuldu.")
#     def whoAmI(self):
#         print("I am i person")
          
# class Student(Person):
#     def __init__(self) -> None:
#         super().__init__()
#        # Person.__init__(self)
#         print("Ogrenci olusturuldu.")

# person1=Person()
# student1=Student()
# # İnhertance biraz karısık bir daha bakılabilir
# print(person1.whoAmI()) 
# print(student1.whoAmI()) #student kalıtım aldığı için fonksiyona bu da erişebiliyor 

# # ezme işlemleri biraz sıkıntılı 
# # override kısmına bir bakılabilir 
# # 8.4 kısım 6. yer kalılnan  

# Bir tur daha izleyeceğim

# class Person:
#     def __init__(self) -> None:
#         print("Person Created")


# class Student(Person):
#     pass

# p1=Person()  #kalıtım alınan sınıftan nesne üretilince otomatik kurucu ekrana bir şeyler yazacak 
# s1=Student() #kalıtım alan nesne de aynı şekilde person sınıfının kurucusunu cagiracak ve çalıştıracak



# class Person:
#     def __init__(self) -> None:
#         print("Person Created")


# class Student(Person):
#     def __init__(self) -> None:
#         super().__init__() # bu olmasa student classının kurucusu person kurucusunu ezer ve yazdırmaz ama bu olunca hem kendininkini
#         print("Student Create") #hem de kalıtım aldığı sınıfn kurucusunu çalıştırıyor.

# p1=Person()  
# s1=Student()




