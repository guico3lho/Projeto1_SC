from assets import desafio_2, desafio_2, lf_portuguese, lf_english
from functions_1 import filter_regex, decryption
import string
from functions_2 import coincidences_function
import os


##### ABREVIAÇÕES IMPORTANTES PARA ENTENDER O CÓDIGO #####

# lf = letter frequency
# dict = dictionary

############################################################

cipherText = input("Coloque o texto a ser decifrado:")
os.system('cls' if os.name == 'nt' else 'clear')

key_size = None

filtered_cipher = filter_regex(cipherText)

possibleKeySize = coincidences_function(filtered_cipher)


print("-------------AVISO-------------")
print("Lembrando que quanto maior o tamanho da chave e maior o número de ocorrências no dicionário abaixo, maior a chance de ser o tamanho certo")
print("-------------AVISO-------------")

# options for the choosing key
print(possibleKeySize)
key_size = int(
    input("Escolha o tamanho de chave desejado com base no dicionário acima:"))
os.system('cls' if os.name == 'nt' else 'clear')
print("EN (1)")
print("PT-BR (2)")

condition = True
while condition:
    lf_option = int(input(
        "Escolha a lingua da tabela de frequencias a ser utilizada: "))
    os.system('cls' if os.name == 'nt' else 'clear')
    if lf_option == 1:
        lf = lf_english
        condition = False
    elif lf_option == 2:
        lf = lf_portuguese
        condition = False

# RVGLLAKIEGTY - ciphertext without numbers and ponctuations
cipherText_filtered = filter_regex(cipherText).upper()


dict_of_dicts = {}  # dictionary that holds ${iterator} dictionaries

dict_of_dicts_frequency = {}


iterator = 0  # iterator to pick frequency of letters
while iterator < key_size:

    dict_of_lf_ciphertext = dict.fromkeys(string.ascii_uppercase, 0)
    dict_of_lf_ciphertext_freq = dict.fromkeys(string.ascii_uppercase, 0)

    # percorre o ciphertext de ${key} em ${key} até o final. Faz isso para L1,L2,...,LN, sendo N = key_size
    for i in range(iterator, len(cipherText_filtered), key_size):
        dict_of_lf_ciphertext_key = cipherText_filtered[i]  # R, A, ...

        # caso encontre a letra, aumenta a sua quantidade no dicionário
        dict_of_lf_ciphertext[dict_of_lf_ciphertext_key] = dict_of_lf_ciphertext.get(
            dict_of_lf_ciphertext_key) + 1

    # adiciona o dicionário criado no dicionario de dicionarios
    dict_of_dicts_key = 'H' + str(iterator)

    # ordena o dict alfabeticamente para auxiliar no processo de descobrir as letras da chave
    dict_of_lf_ciphertext = dict(sorted(dict_of_lf_ciphertext.items()))

    # armazenar o numero total de letras
    total = 0
    for letter, quantity in dict_of_lf_ciphertext.items():
        total += quantity
    # pegar a ocorrencia e dividir pelo total
    dict_of_dicts_frequency_key = 'F' + str(iterator)

    for (letter, frequency), (letter2, quantity) in zip(dict_of_lf_ciphertext_freq.items(), dict_of_lf_ciphertext.items()):
        frequency = round(quantity*100/total, 2)

        dict_of_lf_ciphertext_freq[letter] = frequency

    dict_of_dicts_frequency[dict_of_dicts_frequency_key] = dict_of_lf_ciphertext_freq
    dict_of_dicts[dict_of_dicts_key] = dict_of_lf_ciphertext
    iterator += 1


lf = dict(sorted(lf.items()))


# Criando o jogo para shiftar as frequencias
key = ""
operation = None
remain_letters_of_key = len(dict_of_dicts_frequency.items())
for letter, table_frequency in dict_of_dicts_frequency.items():

    # print(letter, table_frequency)
    operation = None
    while operation != 'quit':
        if(lf == lf_english):
            print("------------ English Frequency Table ---------\n", lf)
        if(lf == lf_portuguese):
            print("------------ Portuguese Frequency Table ---------\n", lf)

        print("------------" + letter +
              " Table --------------\n", table_frequency)

        print("\nAperte [S + Enter] para deslocar o dict " +
              letter + " uma vez")
        print("Aperte [A + Enter] para adicionar a letra mais a esquerda do dict " +
              letter + " na chave")
        print("Escreva \"quit\" para sair")
        print("Falta escolher " + str(remain_letters_of_key) + " letras da chave\n")
        operation = input("Escolha a operação desejada:")

        if(operation == 'A'):
            # Adicionar letra a chave
            key += next(iter(table_frequency))
            print("Letra adicionada:", next(iter(table_frequency)))
            print("Chave até o momento:", key)
            remain_letters_of_key -= 1
            operation = 'quit'

        if(operation == 'S'):
            # implementa o shift
            key_to_be_deleted = next(iter(table_frequency))  # A
            value_to_be_deleted = table_frequency[key_to_be_deleted]  # 0
            # Deletou A do dicionario
            del table_frequency[key_to_be_deleted]
            # Adicionou A no final do dicionario
            table_frequency[key_to_be_deleted] = value_to_be_deleted
            print("Chave até o momento:", key)

decoded_text = decryption(cipherText_filtered.lower(), key)
print("Texto decodificado:\n", decoded_text)
print("Caso o texto tenha sido decodificado errado, experimente utilizar um outro tamanho de chave")
