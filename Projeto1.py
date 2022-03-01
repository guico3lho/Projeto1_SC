import numpy as np
import string
from assets import alphabet

plaintext = "Eu gosto de banana"
            #eugostodebanana
            #chaveschavescha

cipher_text = ""

plaintext_filtered = plaintext.replace(" ", "").lower()

plaintext_array = np.array(list(plaintext_filtered))
key = np.array(list("chaves"))

keys_list = list(alphabet)

while len(plaintext_array) >= 1:

  
  # dar match da key com o plaintext (deixar mesmo tamanho) 
  for i in range(len(key)):
    print("p_l", plaintext_array[0])
    print("k_l", key[i])

    plaintext_alphabet_value = alphabet.get(plaintext_array[0]) # e - 5
    key_alphabet_value = alphabet.get(key[i]) # c - 3

    print(plaintext_alphabet_value, key_alphabet_value)
    cipher_alphabet_value = (plaintext_alphabet_value+key_alphabet_value) % 26 # 6
    cipher_text = cipher_text + keys_list[cipher_alphabet_value]
    print('key_value', keys_list[cipher_alphabet_value])

     
    plaintext_array = np.delete(plaintext_array,0)
    if len(plaintext_array) == 0:
      break
print(cipher_text.upper())

