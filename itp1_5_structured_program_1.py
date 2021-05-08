#A:Print a Ractangle
while True:
  h, w = map(int, input().split())
  if h == 0 and w == 0:
    break
  for i in range(h):
    print('#'*w)
  print()

#B:Print a Flame
while True:
  h, w = map(int, input().split())
  if h == 0 and w == 0:
    break
  for i in range(h):
    if i == 0 or i == h-1:
      print('#'*w)
    else:
      print('#' + '.'*(w-2) + '#')
  print()

#C:Print a Chessboard
while True:
  h, w = map(int, input().split())
  if h == w == 0:
    break
  for i in range(h):
    if i%2 == 0:
      for j in range(w):
        print('#' if j%2 == 0 else '.', end='')
    else:
      for j in range(w):
        print('.' if j%2 == 0 else '#', end='')
    print()
  print()
"""
=========== もっとスマートなforループ ===========
for i in range(h):
  print(''.join('#.'[(i + j) % 2] for j in range(w)))

文字列 '#.' を(i + j)を2で割った余り[0または1]を使ってスライスしている。
"""

#D:Structured Programming
n = int(input())
result = []
for i in range(1, n+1):
  if i%3 == 0 or '3' in str(i):
    result.append(i)
print(' '.join(map(str, result)))