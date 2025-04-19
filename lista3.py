#lista itensional
#S={2.x/xE N, x <= 10} ejemplo
a = [2*x for x in range(1,11)]
print(a)

print()
#agora nuemros impares
b = [x for x in range(1,10,2)]
print(b)

print()
#ahora si los multiplos de 3 son 0

print([0 if x % 3 ==0 else x for x in range(1,10,2)])

print()
