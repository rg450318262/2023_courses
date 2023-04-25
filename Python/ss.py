# Function to calculate the sum of squares of a list of numbers

def sum_of_squares(numbers):
    total = 0
    for n in numbers:
        total += n*n
    return total

def main():
    numbers = [1, 2, 3, 4, 5]
    print(sum_of_squares(numbers))

if __name__ == '__main__':
    main()