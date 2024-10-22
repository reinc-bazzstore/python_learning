import random

# ランダムな数を生成
number_to_guess = random.randint(1, 100)
attempts = 0
guess = None

print("1から100までの数字を当ててください！")

# ユーザーが正解するまで繰り返す
while guess != number_to_guess:
    guess = int(input("予想した数字を入力してください: "))
    attempts += 1

    if guess < number_to_guess:
        print("もっと大きな数字です！")
    elif guess > number_to_guess:
        print("もっと小さな数字です！")

print(f"正解です！ {attempts} 回目で当たりました！")