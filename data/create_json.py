import json
import requests
from datetime import datetime, timedelta

# TMDB api key
API_KEY = '69eed7b4b995f1ec37fd823f0c0aeae8'

# top_rated_movie 전체 출력 테스트
def popular(page):
    url = 'https://api.themoviedb.org/3/movie/top_rated'
    params = {
    'language': 'ko',
    'page': page,
    'api_key': API_KEY,
    }
    file_name = 'top_rated_movie.json'
    add_data_top_rated(url, params, file_name)

# for page in range(1, 470):
#     popular(page)
#     print(page)


# json 파일로 저장하는 함수
def add_data_top_rated(url, params, file_name):
    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()['results']
        for datum in data:
            # vote_average가 7이상인 값만, top_rated_high_vote_average에 저장
            if datum['vote_average'] >= 7:
                django_datum = {
                    "model": "movies.Movie",
                    "pk": datum['id'],
                    "fields": {
                        "genre_ids": datum['genre_ids'],
                        "title" : datum['title'],
                        "original_title" : datum['original_title'],
                        "overview" : datum['overview'],
                        "release_date" : datum['release_date'],
                        "vote_average" : datum['vote_average'],
                        "adult" : datum['adult'],
                        "backdrop_path" : datum['backdrop_path'],
                        "poster_path" : datum['poster_path']
                    }
                }
        # 데이터 json 파일로 저장
                with open(file_name, 'a', encoding='utf-8') as json_file:
                    json_file.seek(0, 2)
                    if json_file.tell() > 0:
                        json_file.write(',')
                    json.dump(django_datum, json_file, ensure_ascii=False, indent=4)
                    json_file.write('\n')
                    print('저장 완료')
    else:
        print('오류 발생', response.status_code)


        
# top_rated_movie 중 vote_average가 7이상인 값만 출력해보기
def top_rated(page):
    url = 'https://api.themoviedb.org/3/movie/top_rated'
    params = {
    'language': 'ko',
    'page': page,
    'api_key': API_KEY,
    }
    file_name = 'movies.json'
    add_data_top_rated(url, params, file_name)

for page in range(1, 470):
    top_rated(page)
#     print(page)
    
def add_data_genres(url, params, file_name):
    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()

        # 데이터 json 파일로 저장
        with open(file_name, 'a', encoding='utf-8') as json_file:
            json_file.seek(0, 2)
            if json_file.tell() > 0:
                json_file.write(',')
            json.dump(data, json_file, ensure_ascii=False, indent=4)
            json_file.write('\n')
            print('저장 완료')
    else:
        print('오류 발생', response.status_code)


def genres():
    url = 'https://api.themoviedb.org/3/genre/movie/list'
    params = {
        'language': 'ko',
        'api_key': API_KEY,
    }
    file_name = 'genres.json'
    add_data_genres(url, params, file_name)

# genres()

def add_data_top_rated(url, params, file_name):
    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()['results']
        for datum in data:
            # vote_average가 7이상인 값만, top_rated_high_vote_average에 저장
            if datum['vote_average'] >= 7:
        # 데이터 json 파일로 저장
                with open(file_name, 'a', encoding='utf-8') as json_file:
                    json_file.seek(0, 2)
                    if json_file.tell() > 0:
                        json_file.write(',')
                    json.dump(datum, json_file, ensure_ascii=False, indent=4)
                    json_file.write('\n')
                    print('저장 완료')
    else:
        print('오류 발생', response.status_code)


# 시작 날짜와 끝 날짜 설정
start_date = datetime(2024, 1, 1)
end_date = datetime(2024, 12, 31)
dates = []

# 시작 날짜부터 끝 날짜까지의 날짜 리스트 생성
current_date = start_date
while current_date <= end_date:
    dates.append(current_date.strftime("%Y-%m-%d"))
    current_date += timedelta(days=1)

def anniversary():
    data = []
    for i in range(1, 367):
        datum = {
            "model": "movies.Anniv",
            "pk": i,
            "fields": {
                "name": "",
                "date": dates[i-1]
            }
        }
        data.append(datum)

    with open('anniversary.json', 'a', encoding='utf-8') as json_file:
        json_file.seek(0, 2)
        if json_file.tell() > 0:
            json_file.write(',')
        json.dump(data, json_file, ensure_ascii=False, indent=4)
        json_file.write('\n')
        print('저장 완료')

# anniversary()

'''
class MovieGenreInfo(models.Model):
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE)
    genre_id1 = models.IntegerField()
    genre_id2 = models.IntegerField(null=True)
    genre_id3 = models.IntegerField(null=True)
    genre_id4 = models.IntegerField(null=True)
    genre_id5 = models.IntegerField(null=True)
'''

cnt = 1

# json 파일로 저장하는 함수
def add_movie_genre_info(url, params, file_name):
    global cnt
    response = requests.get(url, params=params)

    
    if response.status_code == 200:
        data = response.json()['results']
        for datum in data:
            # vote_average가 7이상인 값만, top_rated_high_vote_average에 저장
            if datum['vote_average'] >= 7:
                django_datum = {
                    "model": "movies.MovieGenreInfo",
                    "pk": cnt,
                    "fields": {
                        "movie_id": datum['id'],
                    }
                }
                cnt += 1
                for i in range(len(datum['genre_ids'])):
                    if i > 4:
                        break
                    django_datum['fields']['genre_id'+str(i+1)] = datum['genre_ids'][i]

        # 데이터 json 파일로 저장
                with open(file_name, 'a', encoding='utf-8') as json_file:
                    json_file.seek(0, 2)
                    if json_file.tell() > 0:
                        json_file.write(',')
                    json.dump(django_datum, json_file, ensure_ascii=False, indent=4)
                    json_file.write('\n')
                    print('저장 완료')
    else:
        print('오류 발생', response.status_code)

        
# top_rated_movie 중 vote_average가 7이상인 값의 영화 장르 정보를 저장
def movie_genre(page):
    url = 'https://api.themoviedb.org/3/movie/top_rated'
    params = {
    'language': 'ko',
    'page': page,
    'api_key': API_KEY,
    }
    file_name = 'movie_genre_info.json'
    add_movie_genre_info(url, params, file_name)

# for page in range(1, 470):
#     movie_genre(page)
#     print(page)