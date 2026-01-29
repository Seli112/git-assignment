def sum_even_numbers(start, end):
    """
    Calculate the sum of all even numbers between start and end (inclusive).
    """
    total = 0
    for num in range(start, end + 1):
        if num % 2 == 0:  # Check if number is even
            total += num
    return total

if __name__ == "__main__":
  
    result = sum_even_numbers(1, 100)
    print(f"The sum of all even numbers from 1 to 100 is: {result}")