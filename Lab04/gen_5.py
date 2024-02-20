def countdown(n):
    while n >= 0:
        yield n
        n -= 1

#Sample
n = 5 
print(f"Counting down from {n} to 0:")
for num in countdown(n):
    print(num)