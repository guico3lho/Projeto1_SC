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
    print(filtered_dictionary)
