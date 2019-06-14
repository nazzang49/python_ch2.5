# 출력 구문 내 인자 전송시 step 적어주어도 됨
def incr(a, step=1):
    return a + step

print(incr(5))
print(incr(10))
print(incr(10,4))

# 키워드 인수
def area(width, height):
    return width*height

print(area(10,5))
print(area(height=10, width=5))
print(area(10,5))

def varg(a, *arg):
    print(a, arg)

varg(1)
varg(1, 2)
varg(1, 2, 3, 4, 5)

def _print(*args, end='newline'):
    print(args,end)

_print(10,20,30)
_print(10,end='tab')
_print(10,'tab')

def printf(format, *args):
    print(format%args)

printf('%s이 %d원짜리 동전을 들고 %d번지를 걷고 있다.', '박진영', 500, 25)

# 정의되지 않은 키워드 인수 처리하기 by dict
def f(width, height, **kw):
    print(width, height)
    # 자동으로 dict 처리됨
    print(kw)

f(10, 20, depth=10, dimension=3)

# 고정 + 가변(*) + 키워드(**)
def g(a, b, *args, **kw):
    print(a, b)
    print(args)
    print(kw)

g(10, 20, 30, 40, 50, c=60, d=70)

# 튜플 및 사전 파라미터 처리 방법
# 튜플 = *파라미터명 / 사전 = **파라미터명 (인수명과 자동 바인딩 됨)
def h(name, age, height):
    print(name, age, height)

h('둘리', 10, 150)
t = ('둘리', 10, 150)
h(*t)

d = {'name':'둘리', 'age':10, 'height':150}
h(**d)








