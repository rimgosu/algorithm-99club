import random
import string

def generate_random_string(length):
    # 알파벳 대소문자와 숫자를 포함한 문자들
    characters = string.ascii_letters + string.digits
    # 지정된 길이만큼 무작위로 문자들을 선택하여 결합
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string

# 20글자 무작위 문자열 생성
result = generate_random_string(20)
print(result)