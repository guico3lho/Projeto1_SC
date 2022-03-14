# utilizado para remover valores de chaves menores que dois
def filter_dictionary(dictionary):
    filteredDictionary = {}
    for key, value in dictionary.items():
        if len(value) > 2:
            filteredDictionary[key] = value
    return filteredDictionary

# utilizado para remover valores de chaves menores que a média de todos os valores


def filter_dictionary2(dictionary, mean):
    filteredDictionary = {}
    for key, value in dictionary.items():
        if value > mean:
            filteredDictionary[key] = value
    return filteredDictionary


def coincidences_function(ciphertext):
    # procura os trios que se repetem
    dictionaryWithTriagrams = {}
    for i in range(len(ciphertext)):
        valueTriagram = ciphertext[i:i+3]  # 0 ao 2 # tps
        # ignora o que é menor que trigrama
        # no fim do texto normalmente é coletado algo menor que trigrama. Isso é descartado
        if len(valueTriagram) < 3:
            break
        if dictionaryWithTriagrams.get(valueTriagram):  # 'trigrama' :
            dictionaryWithTriagrams[valueTriagram].append(
                i)  # 'tps' : [0,2065]
        else:
            dictionaryWithTriagrams[valueTriagram] = [i]

    # queremos apenas trigramas que ocorram mais de 2 vezes
    filtered_dictionary = filter_dictionary(dictionaryWithTriagrams)
    return gettingThePossibleKeyLength(filtered_dictionary)


def gettingThePossibleKeyLength(dictionary):
    dictionaryListed = list(dictionary)  # ['exi', 'ttg', 'acw']
    dictionaryOfPossibleKeyLength = {}

    novoDicionario = {}

    for key in dictionaryListed:  # ['exi']
        listOfValues = dictionary[key]  # [6, 752, 1816]
        for possiblekeys in range(3, 21):  # 2 a 19
            for i in range(len(dictionary[key])):  # 3
                try:
                    spacing = listOfValues[i] - listOfValues[i+1]  # 752 - 6
                    if spacing % possiblekeys == 0:  # possui x no spacing
                        # { 2: [0,1] }
                        if dictionaryOfPossibleKeyLength.get(possiblekeys):
                            dictionaryOfPossibleKeyLength[possiblekeys].append(
                                i)
                            novoDicionario[possiblekeys] = len(
                                dictionaryOfPossibleKeyLength[possiblekeys])
                        else:
                            dictionaryOfPossibleKeyLength[possiblekeys] = [
                                i]  # {2: [0]}
                except:
                    break

    # dicionario filtrado considerando a média dos valores
    novoDicionario = dict(sorted(novoDicionario.items()))

    total = 0
    tamanhoNovoDicionario = len(novoDicionario)
    for key, value in novoDicionario.items():
        total += value
    mean = total/tamanhoNovoDicionario
    filteredDictionary = filter_dictionary2(novoDicionario, mean)

    return filteredDictionary
