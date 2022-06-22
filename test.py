def greet(name: str):
    print(f"hello, {name}")


def main():
    for name in "name1", "name2", "name3":
        greet(name)


if __name__ == "__main__":
    main()
