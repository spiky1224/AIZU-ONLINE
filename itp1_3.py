#A:Print Many Hello World
for i in range(1000):
  print('Hello World')

#B:Print Test Cases
idx = 1
while True:
  n = input()
  if n == '0':
    break
  print("Case {}: {}".format(idx, n))
  idx += 1

#C:Swapping Two Numbers
while True:
  x, y = map(int, input().split())
  if x == 0 and y == 0:
    break
  elif x > y:
    x, y = y, x
  print("{} {}".format(x, y))

#D:How Many Divisors
a, b, c = map(int, input().split())
count = 0
for d in range(a, b+1):
  if c%d == 0:
    count += 1
print(count)