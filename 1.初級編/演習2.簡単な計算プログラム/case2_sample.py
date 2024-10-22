# 足し算、引き算、掛け算、割り算を行う簡単な計算機
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "ゼロで割り切れません。"
    return x / y

# メインプログラム
print("Select operation:")
print("1. Add (加算): +")
print("2. Subtract (減算): -")
print("3. Multiply (乗算): *")
print("4. Divide (除算): /")

choice = input("実行する演算子を選択してください。 (1/2/3/4): ")

num1 = float(input("最初の数字を入力してください。: "))
num2 = float(input("2番目の数字を入力してください。: "))

if choice == '1':
    print(f"{num1} + {num2} = {add(num1, num2)}")
elif choice == '2':
    print(f"{num1} - {num2} = {subtract(num1, num2)}")
elif choice == '3':
    print(f"{num1} * {num2} = {multiply(num1, num2)}")
elif choice == '4':
    print(f"{num1} / {num2} = {divide(num1, num2)}")
else:
    print("Invalid input")