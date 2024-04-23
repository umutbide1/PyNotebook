# range() methodu 

for item in range(10): # bu mesela 10 a kadar 
    print(item)
 


for item in range(50,100,10):  # burada mesela 50 den başla 100 e kadar git ve 10 ar 10 ar ilerle demek  
    print(item)  

print(list(range(50,100,20))) # liste şeklinde ekrana yazdırmak için kullanılabilir

#enumrate 

greeting="Hello There"

for letter in enumerate(greeting):
    print(letter)


#zip methodu  iki listeyi biribir ile eşlemek için kullanılıyor aslında bu dictionary kısmında da yapılıyordu bu da ayrı bir gösterim aslında 
 
list1=[1,2,3,4,5]
list2=["a","b","c","d","e"]

print(list(zip(list1,list2)))

# neyin neye karşılık geldiğini anlamaya çalışıyoruz şuan 
# eğer 3 tane birleştirme muhabbetimiz olsaydı gene aynı muhabbet üçünü birden birleştirirdi 