# 선 로컬 변수 탐색 / 후 글로벌 변수 탐색
x = 1
def func(a):
    return a + x

# 함수 실행 전 변수를 사용할 수 있도록 x 선언
print(func(10))

x = 1
def func2(a):
    x = 2
    return a + x

# 12 (x = 로컬 변수)
print(func2(10))
# 1 (x = 글로벌 변수)
print(x)
print(dir('__builtins__'))

g = 1
def func3(a):
    global g
    g = 3
    return a + g

print(func3(10))
print(g)
