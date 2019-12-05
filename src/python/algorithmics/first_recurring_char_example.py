from algorithmics.first_recurring_char import first_recurring_char


def main() -> None:
    s = "DBCABA"
    r = first_recurring_char(s)
    print(f"First recuring char in {s} is {r}")


if __name__ == "__main__":
    main()
