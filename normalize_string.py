# 문자열 데이터를 분석하기 전 처리함수 만들기

# 1) 공백 제거
# 2) 불필요한 문자 부호 제거
# 3) 대소문자 구분
import re

states = ['Alabama', ' Georgia!', 'Georgia ', 'georgia', 'FlOrIda', 'south carolina   ', 'West virginia?']
def clean_strings(strings):
        results = []
        # string = 리스트 내 각 단어
        for string in strings:
            # 양쪽 공백 제거
            string = string.strip()
            # 문자 부호 제거하는 정규 표현식(문자 부호 -> 공백)
            string = re.sub('[!#?]', '', string)
            # 각 단어별 첫글자 대문자로 변경 + 나머지는 소문자로
            string = string.title()
            results.append(string)
        return results

print(clean_strings(states))

# def f_strip(string):
#     return string.strip()

def f_sub(string):
    return re.sub('[!#?]', '', string)

# def f_title(string):
#     return string.title()

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
states = clean_strings(states, str.strip, str.title, f_sub)
print(states)
