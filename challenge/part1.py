# 基本構文

# 3つの異なる文字列を出力
print('test')
print('sample')
print('dummy')

# 変数が１０未満だったらメッセージを出力する
# 変数が１０より大きく２５以下だったら更に別にメッセージを出力する
number = 0
if number < 10:
    print('10未満です')
elif number <= 25:
    print('10以上で25以下です')
else:
    print('それ以外です')

# 余りを表示
print(10 % 3)

# 商を表示
print(10 // 3)

# ageでなんかしらの処理
age = 28
if age >= 25 and age < 35:
    print('アラサーですね')
else:
    print('アラサーじゃないですね')

