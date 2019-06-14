def dummy():
    pass

def my_function():
    print('Hello World')

def times(a,b):
    return a*b

def none():
    return

def my_function2(f):
    print(f)

dummy()
my_function()
print(times(5,5))
print(none())
f = my_function
my_function2(f)
print(f, my_function)

# 여러 return 값
def func():
    return 10, 'hello', {1,2,3}
n, s, st = func()
print(n,s,st)

# 파이썬은 기본적으로 call by reference
# 그러나 immutable / mutable에 따라 결과 다름
def f(t):
    t = 20
a = 10
f(a)
print(a)

def f2(seq):
    seq[0]=5
    return seq

# 시퀀스형의 경우 tuple은 변경 불가
# print(f2((1,2,3)))
print(f2([1,2,3]))








































