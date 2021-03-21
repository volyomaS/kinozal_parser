import requests
from QueryBuilder import QueryBuilder
from MovieLink import MovieLink
from bs4 import BeautifulSoup
import json

if __name__ == "__main__":
    q = QueryBuilder()
    q.add_name("Титаник")
    q.add_year(1997)
    q.add_quality("1080p")
    response = requests.get(q.build())
    soup = BeautifulSoup(response.text, 'lxml')
    ans = []
    for candidate in soup.find_all('td', {"class": "nam"}):
        href = "https://kinozal-tv.appspot.com" + \
               str(candidate).split('>')[1].split()[2].split('"')[1].replace('&amp;', '&')
        response = requests.get(href)
        candidate_soup = BeautifulSoup(response.text, 'lxml')
        quality, video, audio, size, duration, translation = candidate_soup.find('div', id='tabs').text.split('\n')[:6]
        quality = quality.split(':')[1].strip()
        video = video.split(':')[1].strip()
        audio = audio.split(':')[1].strip()
        size = size.split(':')[1].strip()
        duration = duration.split()[1].strip()
        name = candidate.text.split('/')[0]
        translation = translation.split(':')[1].strip()
        releaseYear = candidate_soup.text[
                      candidate_soup.text.find('Год выпуска:') + 13:candidate_soup.text.find('Год выпуска:') + 17]
        releaseYear = int(releaseYear)
        imageLink = candidate_soup.find_all('img', {'class': 'p200'})[0]['src']
        movieLink = MovieLink(name, releaseYear, href, imageLink, quality, size, duration)
        ans.append(movieLink.__dict__)
    with open("./movieLinks.json", 'w') as fout:
        json.dump(ans, fout)
