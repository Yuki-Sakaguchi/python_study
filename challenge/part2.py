# 関数

# 2乗する関数
def nijo(x):
    """
    引数を2乗する.
    :return: int x ** 2.
    :params x:int.
    """
    return x ** 2

print(nijo(10))


# 文字列を出力する関数
def println(text):
    print(text + '\n')

println('文字列を出力')
println('するよ')


# 3つの必須引数と2つのオプション引数
def option(x, y, z, w = 100, h = 200):
    print(x)
    print(y)
    print(z)
    print(w)
    print(h)

option(1, 2, 3, 50, 30)


# 2つの関数からなる関数を作る
def nidewaru(x):
    return x // 2

def yonndekakeru(x):
    return x * 4

result = nidewaru(10)
print(yonndekakeru(result))


# 文字列をfloatに変換する
def comversionFloat(x):
    try:
        return float(x)
    except:
        print('err')

print(comversionFloat('20.13'))