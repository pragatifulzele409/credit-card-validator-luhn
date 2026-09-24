print("Credit card validator")
sum_odd_digits = 0
sum_even_digits = 0
total = 0

card_number = input("Enter a credit card number: ")


card_number = card_number.replace("-", "").replace(",", "").replace(" ", "")

if card_number.isdigit():
    card_number = card_number[::-1]

    
    for x in card_number[::2]:
        sum_odd_digits += int(x)

    
    for x in card_number[1::2]:
        x_doubled = int(x) * 2
        if x_doubled >= 10:
            sum_even_digits += (x_doubled // 10) + (x_doubled % 10)
        else:
            sum_even_digits += x_doubled

    total = sum_odd_digits + sum_even_digits

    if total % 10 == 0:
        print("VALID")
    else:
        print("INVALID")
else:
    print("INVALID INPUT: Please enter numbers only.")