def flatten_list(nested_list: list) -> list:
    flat_list = []
    for sublist in nested_list:
        for item in sublist:
            flat_list.append(item)
    return flat_list

def main():
    nested_list = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
    print(flatten_list(nested_list))

if __name__ == "__main__":
    main()