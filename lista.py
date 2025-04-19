a = ["Juan", 20, 1.8, True]
print(a[len(a)-1]) #antigua forma

print(a[-1])
print(a[-2])

print()

b =  [4,2,6,3]
print(len(b))  # muestra todo
print(sum(b))   #suma 
print(max(b))  #maximo
print(min(b))
print(sum(b)/len(b))  # promedio

print()

c = a+b
print(c)

for x in b:
    print(x)
    
print()

#destructuracion
p= "mesa"
q= "silla"
print(p,q)
tmp = p
p = q
q = tmp
print(p,q)

print()

def suma5(e,f):
    return e+5,f+5
x,y = suma5(2,5)
#print(suma5(2,5))
print(x, y)

print()
#---------------------
busca = 4
if busca in b:
    print("Encontrado")


