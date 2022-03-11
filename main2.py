from assets import desafio_1, desafio_1_teste, lf_english
from functions_1 import filter


##### ABREVIAÇÕES IMPORTANTES PARA ENTENDER O CÓDIGO #####

# lf = letter frequency
# dict = dictionary


############################################################


# len(desafio_1) = 839

# while len(desafio_1) >= 1:



desafio_1_filtered = filter(desafio_1).upper() # RVGLLAKIEGTY - ciphertext without numbers and ponctuations

print(desafio_1_filtered)

key_size = 5 # size of the key used to decode

dict_of_dicts = {} # dictionary that holds ${iterator} dictionaries


iterator = 0 # iterator to pick frequency of letters
while iterator < key_size:
       
    dict_of_lf_ciphertext = {}
    for i in range(iterator, len(desafio_1_filtered),key_size): # percorre o ciphertext de ${key} em ${key} até o final. Faz isso para L1,L2,...,LN, sendo N = key_size
        dict_of_lf_ciphertext_key = desafio_1_filtered[i] # R, A, ...

        # Caso a letra encontrada não esteja no dicionário ainda
        if dict_of_lf_ciphertext.get(dict_of_lf_ciphertext_key) == None: 
            dict_of_lf_ciphertext[dict_of_lf_ciphertext_key] = 1
            
        # Se já está no dicionário, incrementa ocorrência em uma vez
        else:          
            dict_of_lf_ciphertext[dict_of_lf_ciphertext_key] = dict_of_lf_ciphertext.get(dict_of_lf_ciphertext_key) + 1

    # adiciona o dicionário criado no dicionario de dicionarios
    dict_of_dicts_key = 'H' + str(iterator)
    
    #ordena o dict alfabeticamente para auxiliar no processo de descobrir as letras da chave
    dict_of_lf_ciphertext = dict(sorted(dict_of_lf_ciphertext.items()))
    dict_of_dicts[dict_of_dicts_key] = dict_of_lf_ciphertext
    iterator+=1

# printa os dicionarios de frequencia para cada letra da chave desconhecida
for letter_frequency_dict in dict_of_dicts.items(): 
    print(letter_frequency_dict) # tuple

# ordena o dict de lf em ingles
lf_english = dict(sorted(lf_english.items()))
print(lf_english)



