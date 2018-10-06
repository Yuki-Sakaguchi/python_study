# コンテナ

# リストを作ろう
artist_list = [ 'ACIDMAN', 'C&K' ]
print(artist_list)
artist_list.append('秦基博')
print(artist_list)

# 緯度と経度のタプルを作ろう
tuple_list = [
    ('31.111123', '56.881231'),
    ('11.111123', '16.881231')
]

# 特徴の辞書を作る
profile = {
    'name': 'Sakaguchi Yuki',
    'age': 18,
}

# 任意のキーを入力する
key = input('key:')
print(profile[key])

# アーティストの曲
artist = {
    "ACIDMAN": [
        '赤橙',
        '造花が笑う'
    ]
}

# setを使う
s = set([1,2,3])
print(s)