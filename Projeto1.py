import numpy as np
import string
from assets import alphabet

plaintext = input("Escreva o sua mensagem: ")
key = input("Insira a sua chave: ")

cipher_text = ""
decoded_text = ""

plaintext_filtered = plaintext.replace(" ", "").lower()

key = np.array(list("chaves"))

keys_list = list(alphabet)

while len(plaintext_filtered) >= 1:
  # dar match da key com o plaintext (deixar mesmo tamanho) 
  for i in range(len(key)):

    plaintext_alphabet_value = alphabet.get(plaintext_filtered[0]) # e - 5
    key_alphabet_value = alphabet.get(key[i]) # c - 3

    cipher_alphabet_value = (plaintext_alphabet_value + key_alphabet_value) % 26 # 6
    cipher_text = cipher_text + keys_list[cipher_alphabet_value]

    plaintext_filtered = plaintext_filtered[1:]

    if len(plaintext_filtered) == 0:
      break

print(cipher_text.upper())

while len(cipher_text) > 1:
    for i in range(len(key)):
        cipher_text_alphabet_value = alphabet.get(cipher_text[0]) # g - 6
        key_alphabet_value = alphabet.get(key[i]) # c - 2
        
        #Aqui pegamos o valor da letra para descriptografar a mensagem.
        decoded_text_value = (cipher_text_alphabet_value - key_alphabet_value) % 26
        #Começamos a montar a nossa string decriptografada.
        decoded_text = decoded_text + keys_list[decoded_text_value]

        cipher_text = cipher_text[1:]
        
        if (len(cipher_text)) == 0:
            break;

print(decoded_text)
