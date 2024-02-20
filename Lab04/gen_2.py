def generate_even_nembers(n):
    for i in range(n+1):
        if i % 2 == 0:
            yield i

def main():
    try:
        n = int(input("Enter a number: "))
        if n < 0:
            print("Please enter a non-negative number")
            return
        even_numbers = generate_even_nembers(n)
        print("Even numbers between", n, "are: ", end = "")
        print(*even_numbers, sep=", ", end=".\n")
    except ValueError:
        print("Invalid input. Please enter a valid integer")

if __name__ == "__main__":
    main()