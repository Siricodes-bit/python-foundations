"""
Basic practice: Functions + Loops + Conditional Statements
"""

#  Check Even or Odd
def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"


#  Find Sum of First N Natural Numbers
def sum_n_numbers(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total


#  Count Vowels in a String
def count_vowels(text):
    count = 0
    for ch in text.lower():
        if ch in "aeiou":
            count += 1
    return count


#  Print Multiplication Table
def print_table(num):
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")


#  Find Largest Number in a List
def find_largest(numbers):
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    return largest

print(check_even_odd(10))
print("Sum:", sum_n_numbers(5))
print("Vowel count:", count_vowels("Python Programming"))
print_table(3)
print("Largest:", find_largest([10, 25, 3, 8]))
