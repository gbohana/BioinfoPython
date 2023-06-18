t = ('A',  'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'Y')

# letra a: número de elementos na tupla
print(len(t))

#letra b: verificar se 'S' pertence à tupla
print('S' in t)

#letra c: criar uma segunda tupla
t2 = ('P', 'G', 'N', 'Y', 'V', 'W')

#letra d: soma das tuplas
t+= t2
print(t)

#letra e: número de ocorrências de Glicina (G), Asparagina (N) e Cisteína (C)
print(t.count('G'))
print(t.count('N'))
print(t.count('C'))

#letra f: posição da primeira 'N'
print(t.index('N'))

#letra g: 5 últimos elementos da tupla
print(t[-5:])
