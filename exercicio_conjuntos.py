'''
_____________
|           |
|Exercício 1|
|___________|

'''
ferramenta1 = {1.9, 1.8, 5.7, 1.6, 5.8, 1.7, 9.6, 5.9, 9.5, 6.5, 6.2, 1.1, 4.4, 3.5, 2.9, 4.7,
4.6, 5.2, 5.3}
ferramenta2 = {4.7, 3.6, 6.2, 7.1, 7, 5.6, 5.7, 3.4, 3.3, 2.1, 3.8, 3.9, 5, 5.1, 1.9, 9.5,
1.0, 1.3, 5.4}
ferramenta3 = {2.2, 3.3, 5.1, 3, 3.7, 9.1, 8.8, 8.5, 2, 4.1, 6.1, 4.9, 1.1, 0.5, 0.8, 3.2,
6.9, 9.3, 9.5}

# letra a: diferenças entre os conjuntos (1,2) (1,3) e (2,3)
print(ferramenta1.difference(ferramenta2))
print(ferramenta1.difference(ferramenta3))
print(ferramenta2.difference(ferramenta3))

# letra b: intersecções entre (1,2) (1,3) e (2,3)
print(ferramenta1.intersection(ferramenta2))
print(ferramenta1.intersection(ferramenta3))
print(ferramenta2.intersection(ferramenta3))

# letra c: inserir elementos dos conjuntos 2 e 3 no 1
ferramenta1.update(ferramenta2)
ferramenta1.update(ferramenta3)
print(ferramenta1)

# letra d: tamanho do conjunto
print(len(ferramenta1))

'''
_____________
|           |
|Exercício 2|
|___________|

'''
setA = {3, 6, 9, 12, 15, 18, 21, 24, 28, 27}
setB = {2, 6, 8, 10, 14, 16, 18, 20, 22, 24}
setC = {2, 6, 10, 18, 20}
setD = {1, 30, 5, 11, 17, 16, 22, 26}

# letra a: a interseção e diferença entre os conjuntos A e B
print(setA.intersection(setB))
print(setA.difference(setB))

# letra b: o conjunto A e B são disjuntos ao conjunto D?
print(setA.isdisjoint(setD))
print(setB.isdisjoint(setD))

# letra c: o conjunto C é subconjunto de A e B?
print(setC.issubset(setA))
print(setC.issubset(setB))

# letra d: acrescentar os elementos 18, 23, 25, 63 no conjunto D
setD.update([18, 23, 25, 63])
print(setD)
