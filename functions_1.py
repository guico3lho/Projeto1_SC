from assets import alphabet
import re

# cria uma lista contendo apenas as chaves de 'alphabet' -> {'a','b','c',...}
keys_list = list(alphabet)


def filter_regex(plaintext):
    plaintext_filtered = ("".join(re.findall("[a-zA-Z]", plaintext)))
    return plaintext_filtered


def enctyption(plaintext_filtered, key):
    cipher_text = ""
    key = key.lower()

    # Cifração
    while len(plaintext_filtered) >= 1:  # lenght inicial é 15
        # dar match da key com o plaintext (deixar mesmo tamanho)
        for i in range(len(key)):  # 0 a 5 no caso de 'chaves'

            # Utilizando mapeamento na estrutura 'alphabet':
            # pegamos o valor da letra do plaintext
            plaintext_alphabet_value = alphabet.get(
                plaintext_filtered[0])  # e -> 4

            # pegamos o valor da letra do key
            key_alphabet_value = alphabet.get(key[i])  # c -> 2

            # pegamos o valor da letra do plaintext
            cipher_alphabet_value = (
                plaintext_alphabet_value + key_alphabet_value) % 26  # 6

            # utilizando a estrutura 'keys_list', pegamos a letra utilizando o valor obtido acima
            cipher_text = cipher_text + keys_list[cipher_alphabet_value]  # g

            # retira a primeira letra do plaintext pois já foi cifrada
            plaintext_filtered = plaintext_filtered[1:]

            # se não tiver mais nenhum letra do plaintext para cifrar, sai do loop
            if len(plaintext_filtered) == 0:
                break
    return cipher_text


def decryption(cipher_text, key):
    decoded_text = ""
    key = key.lower()
    while len(cipher_text) >= 1:  # length inicial é 15
        for i in range(len(key)):  # 0 a 5 no caso de 'chaves'
            # Utilizando mapeamento na estrutura 'alphabet':

            # pegamos o valor da letra do ciphertext
            cipher_text_alphabet_value = alphabet.get(cipher_text[0])  # g -> 6

            # pegamos o valor da letra do key
            key_alphabet_value = alphabet.get(key[i])  # c -> 2

            # pegamos o valor da letra do decodedtext
            decoded_text_value = (
                cipher_text_alphabet_value - key_alphabet_value) % 26  # 4

            # utilizando a estrutura 'keys_list', pegamos a letra utilizando o valor obtido acima
            decoded_text = decoded_text + keys_list[decoded_text_value]  # e

            # Retira a primeira letra do ciphertext pois foi decifrada
            cipher_text = cipher_text[1:]

            # se não tiver mais nenhuma letra do ciphertext para decifrar, sai do loop
            if (len(cipher_text)) == 0:
                break
    return decoded_text
