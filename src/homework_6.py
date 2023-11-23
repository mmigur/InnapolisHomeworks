def count_cat_occurrences(text: str) -> int:
    count = 0
    words = text.split()
    for word in words:
        if word.lower() == "кот":
            count += 1
    return count

def main():
    text = "Кот по имени кот прыгнул на кота"
    print(count_cat_occurrences(text))

if __name__ == "__main__":
    main()