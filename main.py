
from pydoc import plain
from assets import alphabet
from functions_1 import decryption, enctyption, filter

## Relatório
# Aceita virgula, caixa alta, aceita assado
# Referências
# Como foi feita a cifração e decifração
# Como foi feita a quebra (em quais condições é quebrado?)
# TODO: portugues tende a ter umas palavras maiores, começar o chute dessa forma

plaintext = input("Escreva o sua mensagem: ") # Eu gosto de banana
key = input("Insira a sua chave: ") # chaves

plaintext_filtered = filter(plaintext)

cipher_text = enctyption(plaintext_filtered, key)
decoded_text = decryption(cipher_text,key)

print("Cipher_text", cipher_text.upper())
print("Decoded_text",  decoded_text)