'''
_____________
|           |
|Exercício 1|
|___________|

'''
for i in range(1,151):
    grausC = (i - 32)* 5/9
    print (i, grausC)


'''
_____________
|           |
|Exercício 2|
|___________|

'''
tipos = ['DNA', 'RNA', 'PROTEINA']
componentes = [['A', 'G', 'T', 'C'], ['U', 'C', 'A', 'G'], ['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'Y']]

sequencias = ['ATCDLASKWNWNHTLCAAHCIARRYRGGYCNSKAVCVCRN', 'TATTAACCGGGTTTAAACTAGCATGCATGATTAACCAGTACATCTTTT', 'ATCBDLASKWXWNHTLCAAHCIARRYRGGYCNSJAVCVCRN'] 
resto = {'A'}

for i in range(len(sequencias)):
    for c in range(len(componentes)):
        resto.clear()

        for l in sequencias[i]:
            if not l in componentes[c]:
                resto.add(l)

        if len(resto) == 0:
            print('A sequência', i+1, 'é', tipos[c])
            print()
        else:
            print('A sequência', i+1, 'não é', tipos[c], 'pois contém também:')
            for k in resto:
                print(k, end=' ')
            print()
        print()

'''        
for i in range(len(sequencias)):
    restoDNA = {''}
    restoRNA = {''}
    restoPROTEINA = {''}

    restoDNA.clear()
    restoRNA.clear()
    restoPROTEINA.clear()

    for l in sequencias[i]:
            if not l in componentes[0]:
                restoDNA.add(l)
    
    for l in sequencias[i]:
            if not l in componentes[1]:
                restoRNA.add(l)
    
    for l in sequencias[i]:
            if not l in componentes[2]:
                restoPROTEINA.add(l)
    
    if len(restoDNA) == 0:
        print('A sequência', i+1, 'é DNA')
    
    elif len(restoRNA) == 0:
        print('A sequência', i+1, 'é RNA')
    else:
        if len(restoPROTEINA) == 0:
            print('A sequência', i+1, 'é PROTEINA')
        else:
            print('A sequência', i+1, 'não é nenhum deles')
'''


'''
_____________
|           |
|Exercício 3|
|___________|

'''
seq = 'TATTAACCGGGTTTAAACTAGCATGCATGATTAACCAGTACATCTTTT'

comp = ''
for n in seq:
    if n == 'T':
        comp = comp + 'A'
    elif n == 'A':
        comp = comp + 'T'
    elif n == 'C':
        comp = comp + 'G'
    else:
        comp = comp + 'C'

revSeq = []
rev = ''
for n in comp:
    revSeq.append(n)

while len(revSeq) > 0:
    rev = rev + revSeq.pop()

print(rev)

'''
_____________
|           |
|Exercício 4|
|___________|

'''
x = int(input())
fat = 1
for i in range(1, x+1):
    fat = fat * i

print(fat)

'''
_____________
|           |
|Exercício 5|
|___________|

'''
for i in range(1, 16):
    for j in range(0, 11):
        print(i, 'x ', j, '=', i*j)


'''
_____________
|           |
|Exercício 6|
|___________|

'''
seq = 'VRSSSRTPSDKPVAHVVANPQAEGQLQWLNRRANALLANGVELRDNQLVVPSEGLYLIYSQVLFKGQGCPSTHVLLTHT\
ISRIAVSYQTKVNLLSAIKSPCQRETPEGAEAKPWYEPIYLGGVFQLEKGDRLSAEINRPDYLLFAESGQVYFGIIAL'

dic ={'A':71.03711, 'C': 103.00919, 'D': 115.02694, 'E': 129.04259, 'F': 147.06841,'G': 57.02146, 'H': 137.05891,'I': 113.08406,
'K': 128.09496,'L': 113.08406,'M': 131.04049, 'N': 114.04293,'P': 97.05276,'Q': 128.05858,'R': 156.10111,'S': 87.03203,'T': 101.04768,
'V': 99.06841,'W': 186.07931,'Y': 163.06333}

soma = 0
for i in seq:
    soma += dic[i]

print(soma)

'''
_____________
|           |
|Exercício 7|
|___________|

'''
comp = [47, 41, 40, 40, 40, 43, 45]
id = ['3PSM', '2NY9', '2NY8', '2NZ3', '2E3G', '2E3F', '2E3E']

menor = ''
menorcomp = 100
maior = ''
maiorcomp = 0
soma = 0
for i in range(len(id)):
    if comp[i] < menorcomp:
        menor = id[i]
        menorcomp = comp[i]
    
    if comp[i] > maiorcomp:
        maior = id[i]
        maiorcomp = comp[i]

    soma += comp[i]

# letra a
print('A menor sequência é:', menor, 'de comprimento:', menorcomp)

# letra b
print('A maior sequência é:', maior, 'de comprimento:', maiorcomp)

# letra c
print('A média é', soma/len(id))

# letra d
sortedcomps = comp.sort()
mediana = comp[len(comp)//2]
print('A mediana é', mediana)

'''
_____________
|           |
|Exercício 8|
|___________|

'''
molecula1 = [0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 1]
molecula2 = [0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0]
intersecao = []
uniao = []
for i in range(len(molecula1)):
    intersecao.append(molecula1[i] and molecula2[i])
    uniao.append(molecula1[i] or molecula2[i])

distancia = intersecao.count(1)/uniao.count(1)
print(distancia)