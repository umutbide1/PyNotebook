# bu yöntem for ve while a alternatif bir yöntem sanırım o şekilde anladım.

numbers=[x for x in range(10)]  # bu x değerlerini tek tek bu dizinin içine atabiliyoruz.

# append.(x) x değerini dizinin sonuna attığımız method

numbers2=[x**2 for x in range(10)]
print(numbers2)

numbers2=[x**2 for x in range(10) if x%3==0] #burada da 3 e modu düşünerek ekrana yazdırdım böyle kısıtlarda da koyabiliyorum.
print(numbers2)


results=[x if x%2==0 else "TEK" for x in range(0,10)]  # garip bir kullanim ama burada x eğer modu 0 ise kendisini modu 0 değilse 
                                                       # ekrana tek yazdıracak ve bu işlemi range sayesinde 0 ile 10 arasında yapacak
                                                       # eğer mesela range(1,10,2) olsaydı x i 2 2 arttırırken yapacaktı bu işi 

deneme=[x for x in range(1,10)]
print(deneme)


forIcinList=[]                                                     # iki kullanım da aynı mesela matris mantığına biraz benzettim
for x in range(3):
    for y in range(3):
        forIcinList.append((x,y))
print(forIcinList)

alternatif=[(x,y) for x in range(4342) for y in range(1024)]       # bu da alternatifi

print(alternatif)

# alternatif=[(x,y,z) for x in range(1000) for y in range(100) for z in range(100)] 
# print(alternatif)  

