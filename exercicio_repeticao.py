'''
_____________
|           |
|Exercício 1|
|___________|

'''
# usando for
for i in range(11):
    print(i)

# usando while
i = 0
while i <=10:
    print(i)
    i+=1

'''
_____________
|           |
|Exercício 2|
|___________|

'''
# usando for
for i in range(0, 11, 2):
    print(i)

# usando while
i = 0
while i <=10:
    print(i)
    i+=2

'''
_____________
|           |
|Exercício 3|
|___________|

'''
seq = 'TATTAACCGGTTTAAACTAGCATGCATGATTAACCAGTACATCTTTT'
for n in seq:
    if not n in ['A', 'C', 'G', 'T']:
        print('Não é DNA')
        break
else: 
    print('É DNA')


'''
_____________
|           |
|Exercício 4|
|___________|

'''
for i in range(1, 101):
    for j in range(1, i+1):
        if(i % j == 0):
            print(j, 'é divisor de', i )


'''
_____________
|           |
|Exercício 5|
|___________|

'''
for i in range(2, 1001):
    for j in range(2, i):
        if(i % j == 0):
            break
    else: 
        print(i, 'é primo')


'''
_____________
|           |
|Exercício 6|
|___________|

'''
sequencia = 'VRSSSRTPSDKPVAAAAHVVANPQAEGQLQWLNRRANALLANGVELRDNQLVVPSEGLYLIYSQVLAAAFKGQGCPSTH\
VLLTHTISRIAVSYQTKVNLLSAIKAAASPCQRETPEGAEAKPWYEPIYLGGVFQLEKGDRLSAAAAEINRPDYLLFAESGQVYFGIIAL'
i = 0
while i < len(sequencia):
    pos = sequencia.find('AAA', i)
    if pos != -1:
        print("posição:", pos)
        i = pos + 1
    else:
        break



'''
_____________
|           |
|Exercício 7|
|___________|

'''
lista = ['KTCENLA', 'DTFR','GPCFTDGSC', 'DDHCKNKEHLIK', 'GRCRDDFRC', 'WCTRNC', 'ATC']
maior = ''
for seq in lista:
    if len(seq) > len(maior):
        maior = seq
else:
    print(maior)


'''
_____________
|           |
|Exercício 8|
|___________|

'''
nums = [1, 4 ,6 ,3 ,4 ,5 ,7 ,8 ,9 ,5 ,6 ,7 ,4 ,3 ,5 ,6 ,7 , 8]
soma = 0
for i in nums:
    soma += i

media = soma/len(nums)
print(media)
