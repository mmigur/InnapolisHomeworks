global_variable = 10

def calculate_sum(parameter: int) -> int:
    global global_variable
    enclosing_variable = 10
    local_variable = 5
    return global_variable + enclosing_variable + parameter + local_variable

def main():
    parameter = 15
    result = calculate_sum(parameter)
    print(f"Сумма всех переменных: {result}")


if __name__ == "__main__":
    main()