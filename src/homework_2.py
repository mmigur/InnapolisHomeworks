def get_money_text(number: int) -> str:
    if number % 10 == 1 and number % 100 != 11:
        return f"{number} рубль"
    elif number % 10 in [2, 3, 4] and number % 100 not in [12, 13, 14]:
        return f"{number} рубля"
    else:
        return f"{number} рублей"

def main():
    number = int(input("Введите число монет >> "))
    print(get_money_text(number=number))

if __name__ == "__main__":
    main()