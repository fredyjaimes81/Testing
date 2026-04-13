secret_number = 15
limit = 4
chances = 0
while chances < limit:
    user_guess = int(input("please input your number: "))
    chances += 1
    if user_guess == secret_number:
        print("You win")
        break
    elif user_guess != secret_number:
        if user_guess % 2 == 0:
            print("wrong, but the number is even")
        else:
            print("wrong, and the number is odd")
else:
    print("Game over, the number was 15")
    print("thank you")
# solo un comentario
# Fredy add a print: thank
