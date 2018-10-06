# 正規表現

import re

# 普通に
l = "Beautiful is better than ugly."
matches = re.findall("Beautiful", l)
print(matches)

# 大文字小文字無視
l = "Beautiful is better than ugly."
matches = re.findall("beautiful", l, re.IGNORECASE)
print(matches)

# 前方
l = """Although newve is
often better then
*right* now.
If the implementation
is herd to explain,
If the implementation
is easy to explain,
it may be a good
idea. Namespaces
ar one honking
great idea -- let's
do more of those!"""
matches = re.findall("^If", l, re.MULTILINE)
print(matches)

# 後方
matches = re.findall(",$", l, re.MULTILINE)
print(matches)

# 複数パターン
l = 'Two too.'
matches = re.findall('t[ow]o', l, re.IGNORECASE)
print(matches)

# 数値
l = '123 hi 34 hello.'
matches = re.findall('\d', l, re.IGNORECASE)
print(matches)

# 繰り返し
l = 'two twoo not too.'
matches = re.findall('two*', l, re.IGNORECASE)
print(matches)

# ピリオド
l = '__one__two__three__'
matches = re.findall('__.*__', l, re.IGNORECASE)
print(matches)

matches = re.findall('__.*?__', l, re.IGNORECASE)
print(matches)

# エスケープ
l = 'I love $'
matches = re.findall('\\$', l, re.IGNORECASE)
print(matches)

l = 'The ghost that says boo haunts the loo'
matches = re.findall('.oo', l, re.IGNORECASE)
print(matches)