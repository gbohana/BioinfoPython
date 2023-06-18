seqA = 'LRSSSQNSSDKPVAHVVANHQVEEQLEWLSQRANALLANGMDLKDNQLVVPADGLYLVYSQVLFKGQGCPDYVLLTHTVSLRSSSDK'
seqB = 'KPAAHLIGDPSKQNSLLWRANTDRAFLQDGFSLSNNSLLVPTSGIYFVYSQVVFSGKAYSPKATSSPLYLAHEVQLFSS'
seqC = 'CPQGKYIHPQNNSICCTKCHKGTYLYNDCPGPGQDTDCRECESGSFTASENHLRHCLSCSKCRKEMGQVEISSCTVDRDTVCGCR'

# Exercício 1
if len(seqA) >= 80:
    print(seqA, 'tem tamanho maior ou igual a 80')
if len(seqB) >= 80:
    print(seqB, 'tem tamanho maior ou igual a 80')
if len(seqC) >= 80:
    print(seqC, 'tem tamanho maior ou igual a 80')

# Exercício 2
media = (len(seqA) + len(seqB) + len(seqC))/3

if len(seqA) > media:
    print(seqA, 'tem tamanho maior que a média')
if len(seqB) > media:
    print(seqB, 'tem tamanho maior que a média')
if len(seqC) > media:
    print(seqC, 'tem tamanho maior que a média')

# Exercício 3
if 'H' in seqA and not 'P' in seqA:
    print(seqA, 'contém H mas não P')
if 'H' in seqB and not 'P' in seqB:
    print(seqB, 'contém H mas não P')
if 'H' in seqC and not 'P' in seqC:
    print(seqC, 'contém H mas não P')

# Exercício 4
if(len(seqA) > len(seqB)) and (len(seqA) > len(seqC)):
    print(seqA, 'é a maior de todas')
elif(len(seqB) > len(seqA)) and (len(seqB) > len(seqC)):
    print(seqB, 'é a maior de todas')
else:
    print(seqC, 'é a maior de todas')

# Exercício 5
if(len(seqA) < len(seqB)) and (len(seqA) < len(seqC)):
    if(len(seqB) < len(seqC)):
        print(seqA, seqB, seqC)
    else:
        print(seqA, seqC, seqB)
if(len(seqB) < len(seqA)) and (len(seqB) < len(seqC)):
    if(len(seqC) < len(seqA)):
        print(seqB, seqC, seqA)
    else:
        print(seqB, seqA, seqC)
else:
    if(len(seqB) < len(seqA)):
        print(seqC, seqB, seqA)
    else:
        print(seqC, seqA, seqB)
