# ループ

movie_list = ['ウォーキング・デッド', 'アントラージュ', 'ザ・ソプラノズ', 'ヴァンパイア・ダイアリーズ']
for item in movie_list:
    print(item)

for i in range(25, 51):
    print(i)

for index, item in enumerate(movie_list):
    print(str(index) + ' ' + item)

first_list = [8, 19, 41]
second_list = [9, 1, 33, 831]
added_list = []
for i in first_list:
    for j in second_list:
        added_list.append(i * j)
print(added_list)

ans_list = ['1', '2', '3', '4', '5']
while True:
    a = input('数字を入力してください:')
    if a == 'q':
        print('処理を終了します')
        break
    if a in ans_list:
        print('正解です')
    else:
        print('不正解です')