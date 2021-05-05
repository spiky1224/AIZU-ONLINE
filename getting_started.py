#A:Hello World
print('Hello World')

#B:Cubic
n = int(input())
print(n**3)

#C:Ractangle
a, b = map(int, input().split())
print(a*b, (a+b)*2)

#D:Watch
s = int(input())
print("{}:{}:{}".format(s//3600, s//60%60, s%60))