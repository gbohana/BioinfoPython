'''
_____________
|           |
|Exercício 1|
|___________|

'''
import math
# N: x, y, z; CA: x, y, z; C: x, y, z; O: x, y, z
residuo1 = [[108.304, 100.827, 67.992], [108.477, 100.389, 69.362], [109.907, 100.555, 69.817], [110.821, 100.799, 69.027]]

residuo2 = [[107.670, 101.359, 70.074], [108.477, 100.389, 69.362], [109.513, 101.011, 68.450], [110.667, 100.572, 68.425]]

somatorio = (residuo1[0][0] - residuo2[0][0])**2 + (residuo1[0][1] - residuo2[0][1])**2 + (residuo1[0][2] - residuo2[0][2])**2 +\
(residuo1[1][0] - residuo2[1][0])**2 + (residuo1[1][1] - residuo2[1][1])**2 + (residuo1[1][2] - residuo2[1][2])**2 +\
(residuo1[2][0] - residuo2[2][0])**2 + (residuo1[2][1] - residuo2[2][1])**2 + (residuo1[2][2] - residuo2[2][2])**2 +\
(residuo1[3][0] - residuo2[3][0])**2 + (residuo1[3][1] - residuo2[3][1])**2 + (residuo1[3][2] - residuo2[3][2])**2

'''
N1 = [108.304, 100.827, 67.992]
CA1 = [108.477, 100.389, 69.362]
C1 = [109.907, 100.555, 69.817]
O1 = [110.821, 100.799, 69.027]

N2 = [107.670, 101.359, 70.074]
CA2 = [108.477, 100.389, 69.362]
C2 = [109.513, 101.011, 68.450]
O2 = [110.667, 100.572, 68.425]


somatorio = (N1[0] - N2[0])**2 + (N1[1] - N2[1])**2 + (N1[2] - N2[2])**2 +\
(CA1[0] - CA2[0])**2 + (CA1[1] - CA2[1])**2 + (CA1[2] - CA2[2])**2 +\
(C1[0] - C2[0])**2 + (C1[1] - C2[1])**2 + (C1[2] - C2[2])**2 +\
(O1[0] - O2[0])**2 + (O1[1] - O2[1])**2 + (O1[2] - O2[2])**2
'''

RMSD = math.sqrt((1/4) * somatorio)
print(RMSD)

'''
_____________
|           |
|Exercício 2|
|___________|

'''
seqA = 'ATGATCTCGTAATTAACCGGAATTTTGGGCC'
seqB = 'GGCCTTAAGTTTAACCCGGAATTTAAAGGCCCCAAA'

conteudoGC_A = (seqA.count('G') + seqA.count('C'))/len(seqA)
conteudoGC_B = (seqB.count('G') + seqB.count('C'))/len(seqB)

print(100 * conteudoGC_A)
print(100 * conteudoGC_B)