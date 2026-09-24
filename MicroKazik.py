#МИКРОКАЗИК
import random #модуль для создания рандомных чисел

start = input("Do you want to play the game? (Yes/No) ")
if start == "No":
    print("Goodbye!")
else:
    a = random.randint(1,9)
    b = random.randint(1,9)
    c = random.randint(1,9)

print(a, b, c)

if a == b and b == c:
    print("You win!!!")
else: 
    print("try again")

