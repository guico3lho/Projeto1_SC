import string
from assets import alphabet
from functions_1 import decryption, enctyption

# Relatório
# Aceita virgula, caixa alta, aceita assado
# Referências
# Como foi feita a cifração e decifração
# Como foi feita a quebra (em quais condições é quebrado?)

# TODO: portugues tende a ter umas palavras maiores, começar o chute dessa forma

plaintext = input("Escreva o sua mensagem: ") # Eu gosto de banana
key = input("Insira a sua chave: ") # chaves

cipher_text = ""
decoded_text = ""

plaintext_filtered = plaintext 

# filtrando espaços do plaintext
plaintext_filtered = plaintext_filtered.replace(" ", "")

# filtrando pontuações do plaintext
for i in plaintext_filtered:
  if i in string.punctuation:
    plaintext_filtered = plaintext_filtered.replace(i,"")
  if i in string.digits:
    plaintext_filtered = plaintext_filtered.replace(i,"")

# converte para lower case
plaintext_filtered = plaintext_filtered.lower() # eugostodebanana

# cria uma lista contendo apenas as chaves de 'alphabet' -> {'a','b','c',...}
keys_list = list(alphabet) 

cipher_text = enctyption(plaintext_filtered, key, cipher_text,keys_list)
decoded_text = decryption(cipher_text,key,decoded_text, keys_list)

print("Cipher_text", cipher_text.upper())
print("Decoded_text",  decoded_text)