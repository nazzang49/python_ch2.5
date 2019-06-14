import re


def blahblah(x):
    return x*2

for i in range(10):
    print('{0}:{1}'.format(i, blahblah(i)), end=' ')
else:
    print()

# 람다 = 익명 함수 선언(데이터 처리 시 자주 사용)
for i in range(10):
    # i -> x -> return x*2
    print('{0}:{1}'.format(i, (lambda x: x*3)(i)), end=' ')
else:
    print()

# 심화 내용
states = ['Alabama', ' Georgia!', 'Georgia ', 'georgia', 'FlOrIda', 'south carolina   ', 'West virginia?']
def clean_strings(strings, *funcs):
    results = []
    for string in strings:
        for func in funcs:
            # 순차적으로 특정 작업을 수행하는 함수를 활용해 string을 원하는 단어로 변형
            string = func(string)
        results.append(string)
    return results

# str.strip / str.title은 자바로 치면 클래스 타입의 static 함수
# string -> s
states = clean_strings(states, str.strip, str.title, lambda s:re.sub('[!#?]', '', s))
print(states)
