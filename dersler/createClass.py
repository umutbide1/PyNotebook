class Person:
    #attributelar ve methodlar
  
    
    pass #içerisinin boş olmasına olanak sağlayan yapı 
    def __init__(self,name,year) -> None: #construcer kısmı burası 
        self.name=name
        self.year=year
        print("Init calisti")

p1 = Person(name="Umut",year=2002)  # buradan nesne ürettim denebilir üretildiği ab kurucusu çalışıyor yani
p2 = Person(name="Beyza",year=2001)  # bu şekilde de oluşturulabilir 


    

