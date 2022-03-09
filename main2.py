from assets import desafio_1, desafio_1_teste
from functions_1 import filter
# Dado que a gente sabe a keysize de tamanho 5

# quero pegar a frequencia para a letra 1

# len(desafio_1) = 839

# while len(desafio_1) >= 1:


dict_of_lf_ciphertext = {}

desafio_1_filtered = filter(desafio_1).upper()

print(desafio_1)
print(desafio_1_filtered)

for i in range(0, len(desafio_1_filtered),5):
    key = desafio_1_filtered[i]
    print(key)

    if dict_of_lf_ciphertext.get(key) == None:
        dict_of_lf_ciphertext[key] = 1
        print("Nova chave criada!")

    else:
        print("Valor adicionado em chave criada")
        dict_of_lf_ciphertext[key] = dict_of_lf_ciphertext.get(key) + 1
        print(dict_of_lf_ciphertext)

    






# quero pegar a frequencia para a letra 2





