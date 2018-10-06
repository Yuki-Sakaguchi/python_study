# オブジェクト指向

class Shape:
    def __init__(self, w, l):
        self._width = w
        self._len = l
    def calculate_parimeter(self):
        return self._width * self._len
    def what_am_i(self):
        print('I am a Shape.')

class Rectangle(Shape):
    def what_am_i(self):
        print('I am a Rectangle.')

class Square(Shape):
    def change_size(self, w, l):
        self._width += w
        self._len += l

rect = Rectangle(20, 5)
print(rect.calculate_parimeter())
rect.what_am_i()

square = Square(10, 4)
print(square.calculate_parimeter())
square.change_size(2, -2)
print(square.calculate_parimeter())
square.what_am_i()



class Horse:
    def __init__(self, rider):
        self.rider = rider
    def get_rider_name(self):
        return self.rider.name

class Rider:
    def __init__(self, name):
        self.name = name

taro = Rider('taro')
horse = Horse(taro)
print('私の騎手は{}さんです'.format(horse.get_rider_name()))