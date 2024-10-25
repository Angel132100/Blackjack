card1 = int(input("Enter your card1: "))
card2 = int(input("Enter your card2: "))


card_sum = card1 + card2

is_21_or_over = card_sum >= 21


print("Is your hand 21 or over: ", is_21_or_over)