import sympy as sym
from math import isqrt

def generate_matrix(n):
    matrix = [[(i+1)**2 + (j+1)**2 for j in range(n)] for i in range(n)]
    return sym.Matrix(matrix)

def main():
    # Prompt
    user_number = int(input("Enter a number to classify: "))

    n = 20  # square numbers used
    result_matrix = generate_matrix(n)
    print("Generated Matrix:")
    sym.pprint(result_matrix)

    max_value = max(result_matrix)
    if user_number > max_value:
        print(f"The entered number {user_number} is larger than the maximum value in the matrix.")
        print(f"Please increase the value of 'n' and rerun the program to check this number.")
        return

    unique_numbers = count_unique_numbers(result_matrix)
    print("\nUnique Numbers and Their Counts (Sorted in Ascending Order):")
    sorted_unique_numbers = sorted(unique_numbers.items())
    largest_count = 0
    numbers_with_largest_count = []
    for num, count in sorted_unique_numbers:
        print(f"Number: {num}, Count: {count}")
        if count > largest_count:
            largest_count = count
            numbers_with_largest_count = [num]
        elif count == largest_count:
            numbers_with_largest_count.append(num)

    num_unique_numbers = len(unique_numbers)
    print(f"\nTotal Unique Numbers: {num_unique_numbers}")
    print(f"Numbers with Largest Count ({largest_count}): {numbers_with_largest_count}")

    # Check if user_number exists in the matrix
    if user_number in unique_numbers:
        print(f"\nCircle of radius sqrt({user_number}) contains {unique_numbers[user_number]} integer lattice points.")
        if is_perfect_square(user_number):
            print(f"It's a square number, and its square root is: {isqrt(user_number)}")
        positions = find_positions(result_matrix.tolist(), user_number)  # Convert to list of lists
        print("Positions:")
        for pos in positions:
            print(f"Row: {pos[0]}, Column: {pos[1]}")
    else:
        if is_perfect_square(user_number):
            print(f"Number {user_number} is a square number, and its square root is: {isqrt(user_number)}")
            print("However, it does not appear in the matrix, so it has 4 lattice points.")
        else:
            print(f"Number {user_number} is not a square number.")
            print("And since it does not appear in the matrix, it has 0 lattice points.")

    return

def count_unique_numbers(matrix):
    max_value = max(matrix)
    max_value_sqrt = isqrt(max_value)
    unique_numbers = {}

    # Generate list of square numbers up to max_value_sqrt
    square_numbers = [i**2 for i in range(1, max_value_sqrt + 1)]

    for row in matrix.tolist():
        for num in row:
            if num in unique_numbers:
                unique_numbers[num] += 4
            else:
                unique_numbers[num] = 4

    # Increase count for square numbers
    for square_num in square_numbers:
        if square_num in unique_numbers:
            unique_numbers[square_num] += 4
        else:
            unique_numbers[square_num] = 4

    return unique_numbers

def find_positions(matrix, num):
    positions = []
    for i, row in enumerate(matrix):
        for j, value in enumerate(row):
            if value == num:
                positions.append((i+1, j+1))  # Add 1 to row and column indices
    return positions

def is_perfect_square(n):
    root = isqrt(n)
    return n == root * root

if __name__ == "__main__":
    main()


