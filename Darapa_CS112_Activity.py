def find_smallest_factor(n):
    if n < 2:
        print("Invalid input. Enter a number greater than 2.")
        return

    # Iterate from 2 to the square root of n
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            print(f"The smallest factor of {n} is {i}.")
            return

    # If no factor is found, n is a prime number
    print(f"{n} is a prime number.")

# Get user input for the number
try:
    n = int(input("Enter an integer greater than 2: "))
    find_smallest_factor(n)
except ValueError:
    print("Invalid input. Please enter a valid integer.")