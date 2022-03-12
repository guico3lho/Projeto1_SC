from assets import desafio_1, desafio_1_teste, lf_english
from functions_1 import filter
import string


##### ABREVIAÇÕES IMPORTANTES PARA ENTENDER O CÓDIGO #####

# lf = letter frequency
# dict = dictionary


############################################################


# len(desafio_1) = 839

# while len(desafio_1) >= 1:


# RVGLLAKIEGTY - ciphertext without numbers and ponctuations
desafio_1_filtered = filter(desafio_1).upper()

print(desafio_1_filtered)

key_size = 5  # size of the key used to decode

dict_of_dicts = {}  # dictionary that holds ${iterator} dictionaries

dict_of_dicts_frequency = {}


iterator = 0  # iterator to pick frequency of letters
while iterator < key_size:

    dict_of_lf_ciphertext = dict.fromkeys(string.ascii_uppercase, 0)
    dict_of_lf_ciphertext_freq = dict.fromkeys(string.ascii_uppercase, 0)
    # percorre o ciphertext de ${key} em ${key} até o final. Faz isso para L1,L2,...,LN, sendo N = key_size
    for i in range(iterator, len(desafio_1_filtered), key_size):
        dict_of_lf_ciphertext_key = desafio_1_filtered[i]  # R, A, ...

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
        # print(letter, frequency, letter2, quantity)
        dict_of_lf_ciphertext_freq[letter] = frequency

    # print(dict_of_lf_ciphertext_freq)
    # dict_of_dicts_frequency[dict_of_dicts_frequency_key] =
    dict_of_dicts_frequency[dict_of_dicts_frequency_key] = dict_of_lf_ciphertext_freq
    dict_of_dicts[dict_of_dicts_key] = dict_of_lf_ciphertext
    iterator += 1


# printa os dicionarios de frequencia para cada letra da chave desconhecida
for letter_frequency_dict, letter_frequency_dict_freq in zip(dict_of_dicts.items(), dict_of_dicts_frequency.items()):
    print("\nTable quantity", letter_frequency_dict)  # tuple
    print("\nTable frequency", letter_frequency_dict_freq)

# ordena o dict de lf em ingles
lf_english = dict(sorted(lf_english.items()))
# print(lf_english)
