# 文字列

kamyu = "カミュ"
print(kamyu[0])
print(kamyu[1])
print(kamyu[2])

nani = input('何を書いた？')
dare = input('誰に書いた？')
print("私は昨日、{}を書いて{}に送った".format(nani, dare))

print('aldous Huxley was born in 1894.'.capitalize())

print("だれが？ いつ？ どこで？".split(' '))

text_list = ['The', 'fox', 'jumped', 'over', 'the', 'fence', '.']
print(' '.join(text_list).replace(' .', '.'))

print('A screaming comes across the sky.'.replace('s', '$'))

print('Hemingway'.index('m'))
# hemingway = 'Hemingwaymmmm'
# for i in range(len(hemingway)):
#     if hemingway[i] == 'm':
#         print(i)

print("It's demo.")
print('It\'s demo.')

print("three"+"three"+"three")
print("three"*3)

print("四月の晴れた寒い日で、時計がどれも13時を打っていた。".split('、')[0])