import json
import requests

# TMDB api key
API_KEY = '69eed7b4b995f1ec37fd823f0c0aeae8'

# json 파일로 저장하는 함수
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
        
# top_rated_movie 중 vote_average가 7이상인 값만 출력해보기
def top_rated(page):
    url = 'https://api.themoviedb.org/3/movie/top_rated'
    params = {
    'language': 'ko',
    'page': page,
    'api_key': API_KEY,
    }
    file_name = 'top_rated_high_vote_average.json'
    add_data_top_rated(url, params, file_name)

for page in range(1, 470):
    top_rated(page)
    print(page)
    
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