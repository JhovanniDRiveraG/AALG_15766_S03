w = []
print(w)
w.append("d")
w.insert(0, "b")
w.append("f")
print(w)
print(w.index("d")) #te muetra la posicion

del w[1]
print(w)
w.remove("b")
print(w)

print()
#tubla lista inmodificable
t = ("r","s","t")
print(t)
v = list(t) #asi se combierte en lista
print(v)