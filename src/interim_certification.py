def sort_namelist() -> None:
    students = ['Иван', 'Алиса', 'Петр', 'Ольга', 'Евгения', 'Дмитрий', 'Ли'].sort()
    for i, name in enumerate(students, 1):
        print(f"{i} {name}")

def main():
    sort_namelist()

if __name__ == "__main__":
    main()