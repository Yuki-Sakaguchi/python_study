# データ構造

# スタック（お皿のように上からしか使えない）
class Stack:
    def __init__(self):
        self.items = []
    def is_empty(self):
        """ 値がないか確認 """
        return not self.items
    def push(self, item):
        """ 値を最後に追加 """
        self.items.append(item)
    def pop(self):
        """ 最後の値を取り出す """
        return self.items.pop()
    def peek(self):
        """ 最後の値を取り出すが消さない """
        return self.items[-1]
    def size(self):
        """ 要素の数を返す """
        return len(self.items)


class Queue:
    def __init__(self):
        self.items = []
    def is_empty(self):
        """ 値がないか確認 """
        return not self.items
    def enqueue(self, item):
        """ 最後の値を取り出す """
        self.items.insert(0, item)
    def dequeue(self):
        """ 要素の数を返す """
        return self.items.pop()
    def size(self):
        """ 要素の数を返す """
        return len(self.itmes)