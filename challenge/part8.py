# クラス

import math


class Apple:
    """
    りんごクラス
    """
    def __ini__(self, w, h, c, p):
        """コンストラクタ"""
        self.width = w
        self.height = h
        self.color = c
        self.producing_area = p


class Circle:
    """
    円のクラス
    """
    def __init__(self, r):
        self.radius = r

    def area(self):
        """
        円の面積を求める
        Return 半径 x 半径 x 円周率
        """
        return (self.radius ** 2) * math.pi

circle = Circle(10)
print('面積は[ ' + str(circle.area()) + ' ]です')


class Triangle:
    """
    三角形のクラス
    """
    def __init__(self, w, h):
        self.width = w
        self.height = h
    def area(self):
        return (self.width * self.height) / 2

triangle = Triangle(10, 20)
print('面積は[ ' + str(triangle.area()) + ' ]')


class Hexagon:
    """
    六角形のクラス
    """
    def __init__(self, sl):
        self.side_length = sl
    
    def calculate_perimeter(self):
        return self.side_length * 6

hexagon = Hexagon(10)
print('外周の長さは[ ' + str(hexagon.calculate_perimeter()) + ' ]')