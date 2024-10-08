'''
실습일: 2024.09.10
실습자: 201910852 심기윤
실습내용: 비트 연산자 이용한 대소문자 변환
'''

'''def toggle_case(char):
    if char.isalpha():
        return chr(ord(char) ^ 32)
    else:
        return char

# Example usage
input_char = input("문자 입력: ")

if len(input_char) == 1:
    converted_char = toggle_case(input_char)
    print("변환된 문자: ", converted_char)
else:
    print("문자를 입력하시오")'''

char = input("문자 입력: ")
char = chr(ord(char) ^ 32)
print(char)