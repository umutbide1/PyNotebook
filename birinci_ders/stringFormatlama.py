name="umut"
lastName="Bide"
print("My name is {}" .format(name))  #ilk suslu parantez yerine name bilgisi geldi
print("My name is {} {}" .format(name,lastName))  # bu sefer de iki parametre götürdüm

print("My name is {0} {1}" .format(name,lastName))  # normali bu aslında birinci index ve ikinci index şekinde 

print("My name is {1} {0}" .format(name,lastName)) # yeri değişir mantıken çunku artık once 1. parametreyi cagiracak sonra ikinci parametreyi cağıracak

print("My name is {ln} {s}") .format(n=name,ln=lastName) # burada da bir üst satırın çıktısı gibi bir çıktı alınabilir 

print("My name is {s} {ln}") .format(n=name,ln=lastName) # burada da bir üst satırın tam tersi gibi bir çıktı alınabilir 

result=100/350

print("the result is {r:1.5}") .format(r=result) # bu satirda sunlar oldu 1.5 kısmı sayının ilki en başta kaç bosluk bırakılacagını ve sondaki virgulden sonra kaç basamagının yazılacağını belirledi


