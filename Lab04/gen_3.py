def generate_divisible_by_3_4(n):
    for i in range(n+1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

#Example:
def main():
    try:
        n = int(input("Enter a number: "))
        if n < 0:
            print("Error")
            return
        divisible_numbers = generate_divisible_by_3_4(n)
        print("Numbers divisible by 3 and 4:","are: ", end = "")
        print(*divisible_numbers, sep=", ", end = ".\n")
    except ValueError:
        print("Invalid input")

if __name__ == "__main__":
    main()