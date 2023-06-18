''' 
____________________________________________________________________
|                                                                   |
|                          Exercício 1                              |
|___________________________________________________________________|

'''
tnf = "VRSSSRTPSDKPVAHVVANPQAEGQLQWLNRRANALLANGVELRDNQLVVPSEGLYLIYSQ\
VLFKGQGCPSTHVLLTHTISRIAVSYQTKVNLLSAIKSPCQRETPEGAEAKPWYEPIYLGGVFQLEKGDRLSAEINRPDYLLFAESGQVYFGIIAL"

# Tamanho da sequência
print(len(tnf))

# Contagem da ocorrência de 'LL'
print(tnf.count('LL'))

# Retornar posições de 'GG 'RR'
print(tnf.find('GG'), tnf.find('RR')) 

# Retornar os 100 primeiros aminoácidos
print(tnf[:100])

# Substituir 'SSSR' por 'AAAA'
tnf = tnf.replace('SSSR', 'AAAA')
print(tnf)

# Separar sequência no local da substituição
print(tnf.split('AAAA'))

''' 
____________________________________________________________________
|                                                                   |
|                          Exercício 2                              |
|___________________________________________________________________|

'''

texto = "As proteínas são cadeias polipeptídicas formadas pela ligação peptídica entre resíduos de aminoácidos.\
Existem 20 tipos de aminoácidos comumente encontrados nos seres vivos. A esses aminoácidos, foram\
atribuídas abreviações de 3 letras e símbolos de 1 letra. As abreviações de 3 letras são bastante evidentes\
consistindo nas três primeiras letras do se nome."

# Texto com letras maiúsculas
texto = texto.upper()
print(texto)

# Texto com letras minúsculas
texto = texto.lower()
print(texto)

# Primeiras letras em maiúsculo
texto = texto.title()
print(texto)

# Maiúsculas em minúsculas e vice-versa
texto = texto.swapcase()
print(texto)

''' 
____________________________________________________________________
|                                                                   |
|                          Exercício 3                              |
|___________________________________________________________________|

'''
insulin_signal = "MALWMRLLPLLALLALWGPDPAAA"

# Retornar tamanho da sequência
print(len(insulin_signal))

# Quebrar a sequência no trecho "LLALLALWG"
fragmentos = insulin_signal.split("LLALLALWG")
print(fragmentos)

# Concatenar sequências resultantes
seq = fragmentos[0] + fragmentos[1]
print(seq)

# Substituir "DPAAA" por "LLALL"
print(seq.replace('DPAAA', 'LLALL'))

''' 
____________________________________________________________________
|                                                                   |
|                          Exercício 4                              |
|___________________________________________________________________|

'''
dna =  "GATGGAACTTGACGTAAACCTATATT"

print(dna.replace('T', 'U'))
