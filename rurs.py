def file_size(filename):
   with open(filename) as f:
      return len(f.read())

print("Общее количество символов в файле:",file_size('pokemon_full.json'))


file = open("pokemon_full.json", "r") 
data = file.read().replace(" ","")
data = data.replace(".","")
data = data.replace(",","")
data = data.replace("[","")
data = data.replace("]","")
data = data.replace("(","")
data = data.replace(")","")
data = data.replace(":","")
data = data.replace(";","")
data = data.replace(".","")
data = data.replace("{","")
data = data.replace("}","")
data = data.replace("'","")
data = data.replace('"','')
number_of_characters = len(data)
print('Общее количество символов в файле без пробелов и знаков препинания:', number_of_characters)



word = 'description' 
 
inp = open('pokemon_full.json').readlines()
maxx=0
c=0
for i in iter(inp):
   if word in i:
      c+=1
      
      if len(i)>maxx:
         maxx=len(i)
         im = i
         poryadkovy=c


k=0
name = 'name'
for i in iter(inp):
   if name in i:
      k+=1
      if k==poryadkovy:
         pokem = i
         pokem = pokem.replace("name","")
         pokem = pokem.replace(":","")
         pokem = pokem.replace(",","")
         pokem = pokem.replace('"','')
         print("Покемон с самым длинным описанием:",pokem)


umenia = 'abilities'
a = []
maxx=0
fl=0
for i in iter(inp):
   if umenia in i:
      fl=1
   elif 'stats' in i:
      fl=0
      a = []
   elif fl==1:
      a.append(i)
      if len(a)>maxx:
         maxx = len(a)
         b = a
b = str(b)
b = b.replace('[','')
b = b.replace('"','')
b = b.replace("'","")
b = b.replace(']','')
b = b.replace(',','v')
b = b.replace('n','')
b = b.replace('','')
b ="".join(c for c in b if c.isalpha())
b = b.replace('v',' ')
print('Названия умений, которые содержат больше всего слов:',b)
