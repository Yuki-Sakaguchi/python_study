# もっとオブジェクト指向

class Square:
    square_list = []
    def __init__(self, w, l):
        self._width = w
        self._len = l
        self.square_list.append(self)
    def __repr__(self):
        return '{} by {} by {} by {}'.format(self._len, self._len, self._len, self._len)

s1 = Square(10, 5)
s2 = Square(20, 2)
s3 = Square(30, 4)
print(s1)
print(s2)
print(s3)