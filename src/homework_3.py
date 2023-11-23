def get_fibonacci_number(sequence_number: int) -> int:
    if sequence_number <= 0:
        return "Введите число больше 0"
    elif sequence_number == 1:
        return 0
    elif sequence_number == 2:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, sequence_number):
            a, b = b, a + b
        return b

def main():
    sequence_number = int(input("Введите номер числа в последовательности Фибоначчи: "))
    result = get_fibonacci_number(sequence_number)
    print(f"Число под номером {sequence_number} в последовательности Фибоначчи: {result}")

if __name__ == "__main__":
    main()