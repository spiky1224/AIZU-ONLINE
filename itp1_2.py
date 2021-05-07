#A:Small, Large, Equal
a, b = map(int, input().split())
if a > b:
  print('a > b')
elif a < b:
  print('a < b')
else:
  print('a == b')

#B:Range
a, b, c = map(int, input().split())
if a < b < c:
  print("Yes")
else:
  print("No")

#C:Sorting Three Numbers
print(*sorted(map(int, input().split())))   # * はリストをアンパックして渡す。
# sortedは文字列でしょ？　mapでint型のリストじゃないの？　要調査！！！！
#
#答え　＝＞　sortedは、
#　イテラブルなオブジェクトすべてに対しソート可能で、
#　ソートとしたアイテムをリストにして返す。
#　sortは、リストにのみ適用可能。
#
#答え　＝＞　mapは、
#　リストを受け取り、
#　mapオブジェクトを返す。mapオブジェクトは、イテラブル。

#D:Circle in Ractangle
#(x,y)が、r <= x <= w-r かつ r <= y <= h-r を満たしていれば、Yes
w, h, x, y, r = map(int, input().split())
if r <= x <= w-r and r <= y <= h-r:
  print('Yes')
else:
  print('No')