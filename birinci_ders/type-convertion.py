"""

x=input("1 sayi:")    # bu konsoldan bilgi almaya yariyor ama her defasinda konsoldan kesine kesin bir string ifade alirmiş ama biz 
y= input("2 sayi:")    #string ifade alsin istemiyoruz mesela o zaman tip dönüşümü dediğimiz bir mevzuu bahis ortaya cikiyor 

toplam =x+y

print(toplam)

# eger bu sekliyle cikti alirsam ekrana art arda on ve yirmi yazacak 
a=input("3. sayi:")
b=input ("4. sayi:")
toplam2=int(a)+int(b) 
 
print(toplam2)

# bu kisimda ise integera tip donusumu sagladik 

"""

# x= 5
# y=2.5
# name ="Umut"
# isOnline=True

# int to float 

# x=float(x)
# print(type(x))

# result =str(x)+str(y)
# print(result)
# print(type(result))

# isOnline = str(isOnline)
# print(type(isOnline))
# print(isOnline)

#dairenin alanini ve çevresini hesaplayan program
pi=3.14

halfLenght=float(input("Cemberin yaricapini giriniz "))

#halfLenght=float(halfLenght)

alan=(pi)*halfLenght*halfLenght

cevre=2*(pi)*halfLenght

print("Cemberin Alani:",alan)

print("Cemberin Cevresi",cevre)






