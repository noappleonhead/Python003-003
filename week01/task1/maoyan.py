import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

# Fetch preparation
url = 'https://maoyan.com/films?showType=3'
userAgent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'

# get cookies
# session = requests.Session()
# response = session.get(url)
# print(session.cookies.get_dict())

response = requests.get(url, headers={'user-agent': userAgent})
response.raise_for_status()

# temp data
# bsInfo = bs(open("resp.html"), 'html.parser')
bsInfo = bs(response.text, 'html.parser')

def getTopMovies(num):
    topMovies = bsInfo.find_all(
        'div', attrs={'class': 'movie-item film-channel'})[0:num]
    # loop through each movie
    for movie in topMovies:
        movieHoverInfo = movie.find_all(
            'div', attrs={'class': 'movie-hover-title'})

        result = {'name': None, 'movieType': None, 'releaseDate': None}
        for info in movieHoverInfo:
            # movie name
            name = info.find('span', class_='name')
            if name is not None:
                result['name'] = name.text
                continue

            # movie type
            # release date
            isHoverTag = info.find('span', class_='hover-tag')
            if isHoverTag is not None:
                spanContent = isHoverTag.text
                trimText = info.text.replace('\n', '').replace(' ', '')
                if spanContent == '类型:':
                    result['movieType'] = trimText
                    continue
                if spanContent == '上映时间:':
                    result['releaseDate'] = trimText
                    continue
                
        # write to csv
        currentResult = pd.DataFrame.from_dict(result, orient="index")
        with open("topMovies.csv", 'a') as f:
            currentResult.to_csv(f, header=f.tell()==0)

getTopMovies(10)