'''
_____________
|           |
|Exercício 1|
|___________|

'''
tam_seq = 340
if tam_seq >= 50:
    print('Sequência aceita')
else:
    print('Sequência rejeitada')


'''
_____________
|           |
|Exercício 2|
|___________|

'''
seq = 'AFUISAGBAHBGHSFHSD'

if len(seq) >= 2 and len(seq) <= 50:
    print('É peptídeo')
else:
    print('Não é peptídeo')


'''
_____________
|           |
|Exercício 3|
|___________|

'''
if len(seq) == 2:
    print('É dipeptídeo')
elif len(seq) == 3:
    print('É tripeptídeo')
elif len(seq) >= 4 and len(seq) <= 50:
    print('É polipeptídeo')
else:
    print('Não é peptídeo')


'''
_____________
|           |
|Exercício 4|
|___________|

'''
aa = 'G'

hidrofobico = ['I', 'V', 'L', 'M', 'C', 'A', 'T', 'F', 'Y', 'W', 'H', 'K']
pequeno = ['P', 'A', 'G', 'C', 'S', 'T', 'D', 'N', 'V']
polar = ['C', 'S', 'T', 'N', 'D', 'Q', 'Y', 'W', 'H', 'K', 'R', 'E']
carregado = ['D', 'E', 'R', 'K', 'H']
aromatico = ['F', 'Y', 'W', 'H']
minusculo = ['A', 'C', 'G', 'S']
alifatico = ['I', 'L', 'V']
hidroxila = ['T', 'S']
acido = ['N', 'Q']
enxofre = ['C', 'M']

if aa in hidrofobico:
    print('É hidrofóbico')
if aa in pequeno:
    print('É pequeno')
if aa in polar:
    print('É polar')
if aa in carregado:
    print('É carregado')
if aa in aromatico:
    print('É aromático')
if aa in minusculo:
    print('É minúsculo')
if aa in alifatico:
    print('É alifático')
if aa in hidroxila:
    print('É hidroxila')
if aa in acido:
    print('É ácido')
if aa in enxofre:
    print('É enxofre')


'''
_____________
|           |
|Exercício 5|
|___________|

'''
if not aa in carregado:
    print('É neutro')
if not aa in polar:
    print('É apolar')


'''
_____________
|           |
|Exercício 6|
|___________|

'''
ns_validos = ['A', 'C', 'T', 'G']
purinas = ['A', 'G']
n = 'T'

if n in ns_validos:
    print('É válido')
    if n in purinas:
        print('É purina')
    else:
        print('É pirimidina')
