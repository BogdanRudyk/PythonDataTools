from bs4 import BeautifulSoup
import requests
import shutil
import csv


top_rating = 0
genre = [i for i in input('Какие жанры вас интересуют?\n').split()]

type_anime = input('Какой формат вас интересует? (DVD, Movie, Music, OVA, TV, Web)\n')

episodes = input('Каково максимальное количество эпизодов?\n')
if episodes != '':
    episodes = int(episodes)
else:
    episodes = 99**9

time = input('Какая максимальная длительность? (количество часов)\n')
if time != '':
    time = int(time)
else:
    time = 99**9

rating = input('Какой минимальный рейтинг?\n')
if rating != '':
    rating = float(rating)
else:
    rating = 0

votes = input('Каково минимальное количество голосов?\n')
if votes != '':
    votes = int(rating)
else:
    votes = 0

content_warning = [i for i in input('Какой контент будет неприятен/оскорбителен для вас?\n').split()]


finished = input('Хотите ли вы завершенное аниме или еще идущее? (True или False)\n')

start_year = input('В каком году аниме началось?\n')

end_year = input('В каком году аниме завершилось?\n')

seasons = input('Какой сезон?\n')

studios = input('Какая студия?\n')

f = open('AnimeList.txt', 'w')
with open('anime.csv', encoding='utf-8') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')

    for row in spamreader:
        if row[8] == 'Episodes' or row[8] == 'Unknown':
            row [8] = 9**9
        if row[10] == 'Duration' or row[10] == 'Unknown':
            row[10] = 9**9
        if row[3] == 'Rating Score' or row[3] == 'Unknown':
            row[3] = 0
        if row[4] == 'Number Votes' or row[4] == 'Unknown':
            row[4] = 0
        flag_genre = 0
        if row[5] != 'Tags' and row[5] != 'Unknown':
            for i in range (len(genre)):
                if genre[i] in row[5]:
                    flag_genre = 1
        flag_warning = 1
        if row[6] != 'Content warning' and row[6] != 'Unknown':
            for i in range (len(content_warning)):
                if content_warning[i] in row[6]:
                    flag_warning = 0
        if ((float(row[3]) >= rating or rating == '') and
            (float(row[4]) >= votes or votes == '') and
            (flag_genre == 1 or genre == '') and
            (flag_warning == 1 or content_warning == '') and
            (row[7] == type_anime or type_anime == '') and
            (int(row[8]) <= episodes or episodes == '') and
            (row[9] == finished or finished == '') and
            (int(row[10]) <= time or time == '') and
            (row[11] == start_year or start_year == '') and
            (row[12] == end_year or end_year == '') and
            (row[13] == seasons or seasons == '') and
                (row[14] == studios or studios == '')):
            f.write(row[1] + '\n')
            if float(row[3]) > top_rating:
                top_rating = float(row[3])
                link_to_best_anime = row[16]


html_page = requests.get(link_to_best_anime)
soup = BeautifulSoup(html_page.content, 'html.parser')
warning = soup.find('div', class_="mainEntry")
book_container = warning

images = book_container.findAll('img')
example = images[0]

url_base = "https://www.anime-planet.com/anime/super-robot-wars-og-divine-wars-separate-paths" 
url_ext = example.attrs['src'] 
full_url = 'https://www.anime-planet.com' + url_ext 
r = requests.get(full_url, stream=True) 
if r.status_code == 200:                    
   with open("anime_picture.jpg", 'wb') as f: 
      r.raw.decode_content = True
      shutil.copyfileobj(r.raw, f)




