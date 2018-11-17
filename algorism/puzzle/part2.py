# ランレングス符号化

def encryption(word):
    """
    ランレングス符号化による暗号化.
    :return: string 暗号化された文字列.
    :params word:string.
    """
    if not word or not word.isalpha():
        return False
    word_list = list(word)
    word_list.append('END') # 最後の１文字は計算されないので適当に入れる
    tmp = ''
    count = 0
    ans = ''
    for i, s in enumerate(word_list):
        if tmp and s != tmp:
            ans += str(count) + tmp
            count = 0
        count += 1
        tmp = s
    return ans


def composite(word):
    """
    ランレングス符号化による複合化.
    :return: string 複合化された文字列.
    :params word:string.
    """
    if not word:
        return False
    ans = ''
    for i, s in enumerate(word):
        if s.isalpha():
            ans += s * int(word[i-1])
    return ans

# 文言
word1 = 'BWWWWWBWWWW'
word2 = 'BWBWBWBWBWBWBWBW'

# 暗号化
enc1 = encryption(word1)
enc2 = encryption(word2)
print(enc1)
print(enc2)

# 複合化
comp1 = composite(enc1)
comp2 = composite(enc2)
print(comp1)
print(comp2)

