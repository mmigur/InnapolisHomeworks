def process_operation(operation: str) -> str:
    match operation:
        case "save":
            return "сохранить"
        case "load":
            return "загрузить"
        case _:
            return "неизвестная операция"

def main():
    print(process_operation("save"))
    print(process_operation("load"))
    print(process_operation("delete"))

if __name__ == "__main__":
    main()