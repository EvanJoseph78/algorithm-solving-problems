# Alternative form
# Function to find the missing number
def find_missing_number(n, numbers):
    total_sum = n * (n + 1) // 2  # Sum of all numbers from 1 to n
    given_sum = sum(numbers)      # Sum of the given numbers
    return total_sum - given_sum  # Missing number

# Input
n = int(input())
numbers = list(map(int, input().split()))

# Find and print the missing number
missing_number = find_missing_number(n, numbers)
print(missing_number)


