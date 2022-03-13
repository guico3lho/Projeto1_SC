def filter_dictionary(dictionary):
    filteredDictionary = {}
    for key, value in dictionary.items():
      if len(value) > 2:
        filteredDictionary[key] = value
    return filteredDictionary

def coincidences_function(ciphertext):
    dictionaryWithTriagrams = {}
    for i in range(len(ciphertext)):
      valueTriagram = ciphertext[i:i+3]
      if len(valueTriagram) < 3:
        break
      if dictionaryWithTriagrams.get(valueTriagram):
        dictionaryWithTriagrams[valueTriagram].append(i)
      else:
        dictionaryWithTriagrams[valueTriagram] = [i]
         
    filtered_dictionary = filter_dictionary(dictionaryWithTriagrams)
    gettingThePossibleKeyLength(filtered_dictionary)

def gettingThePossibleKeyLength(dictionary):
    dictionaryListed = list(dictionary)
    dictionaryOfPossibleKeyLength = {}
    for key in dictionaryListed:
        listOfValues = dictionary[key]
        for n in range(20):
            for i in range(len(dictionary[key])):
                try: 
                    delta = listOfValues[i] - listOfValues[i+1]
                    if delta % n == 0:
                        if dictionaryOfPossibleKeyLength.get(n):
                            dictionaryOfPossibleKeyLength[n].append(i)
                        else:
                            dictionaryOfPossibleKeyLength[n] = [i]
                except: 
                    break
    
    print(filter_dictionary(dictionaryOfPossibleKeyLength))
