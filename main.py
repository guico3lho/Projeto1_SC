from functions_1 import decryption, enctyption, filter_regex

plaintext = input("Escreva o sua mensagem: ")  # Eu gosto de banana
key = input("Insira a sua chave: ")  # chaves

plaintext_filtered = filter_regex(plaintext).lower()

cipher_text = enctyption(plaintext_filtered, key)
decoded_text = decryption(cipher_text, key)

print("Cipher_text", cipher_text.upper())
print("Decoded_text",  decoded_text)
