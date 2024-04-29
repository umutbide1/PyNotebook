class Person:
    adress="No Information"
    def __init__(self,name,year) -> None:
        self.name=name
        self.year=year
    # instance method oluşturulan objelere hizmet edeceği için self kullanılmalı 
    def intro(self):
        print("Hello Dear",self.name)
        
    def calculator(self):
        return 2024-self.year
        
    

p1=Person(name="Umut",year=2002)

p1.intro()
print(f"Adim: {p1.name} Yasim: {p1.calculator()}")

class Circle:
    pi=3.14
    def __init__(self,yaricap=1) -> None:
        self.yaricap=yaricap
        
    def cevreHesapla(self):
        return 2*self.pi*self.yaricap
    def alanHesapla(self):
        return self.pi*self.yaricap*self.yaricap
    
    
    
c1=Circle(5)

print(c1.alanHesapla())
print(c1.cevreHesapla())