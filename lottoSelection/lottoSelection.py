import random

print("☆★☆★ 로또 번호 자동 생성기 ☆★☆★")
print("---------------------------------------")
print("게임 수를 입력하세요(숫자만 입력).")

num = input("게임 수 : ")

print("---------------------------------------")

for i in range(0, int(num)):
    lotto = random.sample(range(1, 46), 6)
    lotto.sort()
    print(lotto)

print("---------------------------------------")
print("☆★☆★ 로또 번호 생성완료 ☆★☆★")
print("---------------------------------------")

exit = input("Enter를 누르면 종료됩니다.")

