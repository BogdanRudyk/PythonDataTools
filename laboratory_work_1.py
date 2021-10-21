from os import close, replace

with open ('pokemon_full.json') as f:
   print ('Общее количество символов в файле:', len( f.read() )) # Simple numeral of characters.

with open('pokemon_full.json') as file: 
   data_without_punctuation = file.read().replace(' ', '')
punctuation_marks = ['.', ',', '[', ']', '(', ')', ':', ';', '{', '}', "'", '"'] # List of unnecessary punctuation marks.
for i in range (len(punctuation_marks)):
   data_without_punctuation = data_without_punctuation.replace(punctuation_marks[i], '')
number_of_characters_without_punctuation = len(data_without_punctuation) # Removing unnecessary punctuation marks.
print('Общее количество символов в файле без пробелов и знаков препинания:', number_of_characters_without_punctuation)

pokemon_file = open('pokemon_full.json').readlines()
maximum = 0
counter = 0
for i in iter(pokemon_file):
   if 'description' in i:
      counter += 1
      if len(i) > maximum:
         maximum = len(i)
         serial_number=counter # Finding the desired maximum.
comparison_number = 0 
for i in pokemon_file:
   if 'name' in i and 'named' not in i:
      comparison_number += 1
      if comparison_number==serial_number:
         long_pokemon = i
long_pokemon = long_pokemon.replace('"name"', '').replace(':', '').replace('"', '').replace(',', '') # Search for a pokemon name and remove unnecessary characters.
print('Покемон с самым длинным описанием:', long_pokemon)

roster1 = []
maximum = 0
flag = 0
for i in iter(pokemon_file):
   if 'abilities' in i:
      flag = 1
   elif 'stats' in i:
      flag = 0
      roster1 = []
   elif flag == 1:
      roster1.append(i)
      if len(roster1)>maximum:
         maximum = len(roster1)
         max_roster = roster1 # Finding the longest list of abilities.
most_words_abilities =''
for i in range (len(max_roster)):
   roster_abilities = str(max_roster[i])
   roster_abilities = roster_abilities.replace('"','').replace(',','').replace(']','') # Removing unnecessary characters.
   most_words_abilities += roster_abilities
print('Названия умений, которые содержат больше всего слов: \n', most_words_abilities)
