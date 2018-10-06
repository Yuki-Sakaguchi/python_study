# hangman
import random

def hangman(word):
    """
    ハングマン.
    :params word: str プレイヤーに当ててもらう単語.
    """
    # 間違えた時に表示される絵
    stages = [
        '',
        '______    ',
        '|    |    ',
        '|    O    ',
        '|   /|\   ',
        '|   / \   ',
        '|         ',
    ]
    wrong = 0 # 間違えた回数
    rletters = list(word) # wordを１文字ずつ分解してリストにしたもの
    board = ['_'] * len(word) # プライヤーに見せる内容
    win = False # プレイヤーの勝利フラグ
    
    # ゲーム開始の挨拶！
    print('-----------------------\nハングマンへようこそ！\n-----------------------')
    print(('答えは{}文字です【' + ' '.join(board) + '】').format(len(word)))
    
    # 絵がまだ完成してなければ回答できる
    while wrong < len(stages) - 1:
        print('\n---\n')

        # 回答を取得し、成否を判定
        char = input('１文字を予想してください: ')
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$' # 当たった部分は次に当たらないように文字を入れておく
        else:
            wrong += 1

        # 回答の結果を表示
        print('\n【回答】')
        print(' '.join(board))
        e = wrong + 1
        print('\n【ハングマン】')
        print('\n'.join(stages[0:e]))

        # 勝ちの場合、処理終了
        if '_' not in board:
            print('\n---\n')
            print('あなたの勝ちです')
            print('正解は【{}】でした！'.format(word))
            win = True
            break
    
    # 負けの場合
    if not win:
        print('\n---\n')
        print('\n'.join(stages[0:wrong+1]))
        print('あなたの負けです')
        print('正解は【{}】でした！'.format(word))


def gamestart():
    """
    答えをランダムで選択肢してハングマンを開始する.
    """
    word_list = [
        'banana',
        'apple',
        'cat',
        'coffee',
        'tea',
    ]
    hangman(word_list[random.randint(0, len(word_list)-1)])


# 実行
gamestart()
