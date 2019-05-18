"""
연습문제 4. Mad Libs
명사, 동사, 형용사, 부사를 입력받아서 완성된 이야기를 출력하기!
입출력 예시 :
    입력 화면 – 명사를 입력하세요 : dog 동사를 입력하세요 : walk 형용사를 입력하세요 : blue 부사를 입력하세요 : quickly
    출력 화면 –  Do you walk your blue dog quickly? That’s hilarious!
문장안에 단어를 껴넣는 연습을 하시는 문제입니다. 한글로 만들기에는 문제가 영미 문화권에 속한 부분이라 출력 구문은 영어 그대로 두었습니다.
"""

noun = input("명사를 입력하세요 :")
verb = input("동사를 입력하세요 :")
adjective = input("형용사를 입력하세요 :")
adverb = input("부사를 입력하세요 :")

print("Do you {} your {} {} {}? That’s hilarious!".format(verb, adjective, noun, adverb))