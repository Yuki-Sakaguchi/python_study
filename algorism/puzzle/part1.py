# 帽子を全員で揃える
# このパズルに近いアルゴリズムとして、「ランレングス符号化」がある

# F=前向き、B=後ろ向き
caps0 = []
caps1 = ['F', 'B', 'F', 'B', 'B', 'F', 'B', 'B', 'B', 'F', 'F', 'F', 'B', 'F']
caps2 = ['F', 'F', 'B', 'B', 'B', 'F', 'B', 'H', 'B', 'B', 'F', 'F', 'H', 'F']

def pleaseConformOnepass(caps):
    """
    振り向かせる関数
    先頭の向きが多い方なのは確実です
    なので、先頭と別の向きが振り向かせる対象になる
    :params caps:Array.
    """ 
    if not caps:
        print('引数の配列が空です')
        return False
    caps = caps + [caps[0]] # 一番後ろに先頭と同じ向きを追加（ループでは使われない）
    tmp = 0
    for i in range(1, len(caps)):
        if caps[i] != caps[i-1]: # 一番後ろの向きと違う場合は振り向かせる対象
            if caps[i] != caps[0]: # 振り向かせる開始の位置を保存
                tmp = i
            else: # 振り向かせ初めてから違う向きになったら、その手前までを振り向かせる
                endPosition = i-1
                if endPosition == tmp: # 開始と終わりが一緒なら１つだけ振り向かせる
                    print('People at positions', tmp, 'flip your caps!')
                else: # 開始と終わりに幅があれば、幅分を振り向かせる
                    print('People in positions', tmp, 'through', endPosition, 'flip your caps!')

pleaseConformOnepass(caps1)