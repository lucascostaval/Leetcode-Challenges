from random import randint
import os

while True:
    n1 = randint(0, 1000)
    n2 = randint(0, 1000)
    op = randint(0, 1)
    correct_answer = -1
    if op == 0:
        print(f"{n1}+{n2}=")
        correct_answer = n1+n2
    elif op == 1:
        print(f"{n1}-{n2}=")
        correct_answer = n1-n2
    ans = int(input())
    if ans == correct_answer:
        os.system("cls || clear")
    else:
        print("Errado. Resposta correta:")
        print(correct_answer)
        break