def square(num):
    return num**2

print(square(2)) 
# bu zaten normal kullanım ama şöyle bir kullanım da mevcut 


numbers=[3,5,7,9]
result=list(map(square,numbers))
# burada da map method sayesinde yapıyoruz 

print(result)

result =list(map(lambda num: num**2,numbers))

# bu şekilde bir gösterim de var 
# çok spesifik işlemler nerelerde işimize yarar bilemiyorum.