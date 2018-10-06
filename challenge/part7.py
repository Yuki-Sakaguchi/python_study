# ファイル操作

import csv

# ファイルの読み込み
with open('read.txt', 'r') as f:
    print(f.read())

# ファイルの書き出し
a = input('好きな食べ物は？')
with open('answer.txt', 'w', encoding='utf-8') as f:
    f.write(a)

# csv書き出し
movie_filename = 'movie.csv'
movie_list = [
    ['Top Gun', 'Risky Business', 'Minority Report'],
    ['トップガン', 'リスキービジネス', 'マイノリティリポート'],
    ['Titanic', 'The Revenant', 'Inception'],
    ['Training Day', 'Man on Fire', 'Flight']
]
with open(movie_filename, 'w', encoding='utf-8') as f:
    w = csv.writer(f, delimiter=',')
    for movie_titles in movie_list:
        w.writerow(movie_titles)

# csvの読み込み
with open(movie_filename, 'r', encoding='utf-8') as f:
    r = csv.reader(f, delimiter=',')
    for row in r:
        print(','.join(row))

        