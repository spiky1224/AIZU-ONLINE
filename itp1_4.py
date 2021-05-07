import math

#A:A/B Problem
a, b = map(int, input().split())
print("{} {} {:.8f}".format(a//b, a%b, a/b))
# print(a//b,a%b,f'{a/b:f}')　＜＝ ｆ文

#B:Circle
r = float(input())
print(r*r*math.pi, r*2*math.pi)

#C:Simple Calculator
while True:
  data = input()
  if '?' in data:
    break
  print(int(eval(data)))

#D:Min, Max and Sum
input()
numbers = list(map(int, input().split()))
print(min(numbers), max(numbers), sum(numbers))