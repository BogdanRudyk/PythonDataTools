file = open("pokemon_full.json") 
print ('Общее количество символов в файле:', len( file.read() )) 

# Simple numeral of characters.

file.seek(0)
data_without_punctuation = file.read().replace(' ', '')
punctuation_marks = n\
=['.', ',', '[', ']', '(', ')', ':', ';', '{', '}', "'", '"'] 

# List of unnecessary punctuation marks.

for char_to_cut  in range (len(punctuation_marks)):
   data_without_punctuation = n\
   = data_without_punctuation.replace(punctuation_marks
   [char_to_cut ], '')
amount_no_punctuation = len(data_without_punctuation) 

# Removing unnecessary punctuation marks.

print('Общее количество символов в файле без пробелов \
и знаков препинания:', amount_no_punctuation)

file.seek(0)
pokemon_file = file.readlines()
maximum = 0
counter = 0
for char_to_cut  in pokemon_file:
   if 'description' in char_to_cut :
      counter += 1
      if len(char_to_cut ) > maximum :
         maximum  = len(char_to_cut )
         serial_number=counter # Finding the desired maximum.
comparison_number = 0 
for char_to_cut  in pokemon_file:
   if 'name' in char_to_cut  and 'named' not in char_to_cut :
      comparison_number += 1
      if comparison_number==serial_number:
         long_pokemon = char_to_cut 
unnecessary_chars = ['name', ':', '"', ',', ' ']
for char_to_cut in  unnecessary_chars:
    long_pokemon = long_pokemon.strip()
    long_pokemon = long_pokemon.replace(char_to_cut, '')

 # Search for a pokemon name and remove unnecessary characters.

print('Покемон с самым длинным описанием:', long_pokemon)

most_words_skills  = []
counter = 0
search_range = False
for char_to_cut  in pokemon_file:
   for i in ('\n', ',', '"', "'", '[', ']'):
      char_to_cut = char_to_cut.strip()
      char_to_cut = char_to_cut.replace(i, '')
   if 'abilities' in char_to_cut :
      search_range = True
   elif 'stats' in char_to_cut :
      search_range = False
   elif search_range == True:
      if len(char_to_cut.split()) == counter:
         most_words_skills .append(char_to_cut)
      elif len(char_to_cut.split()) > counter:
         most_words_skills  = [char_to_cut]
         counter = len(char_to_cut.split())

# Easy search for the most words in a skill

print('Названия умений, которые содержат больше всего слов:',
 *most_words_skills )


