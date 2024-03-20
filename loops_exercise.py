numbers = [247, 22, 265, 200, 147, 5, 88, 24, 203, 129, 56, 203, 224, 255, 63, 62, 92, 179, 70, 87, 222, 7, 270, 265, 292, 83, 92, 33, 16, 103, 82, 20, 209, 158, 149, 136, 91, 55, 17, 91, 284, 55, 137, 121, 143, 100, 38, 126, 134, 132]

# Exercise 1: List all even numbers
even_numbers = [num for num in numbers if num % 2 == 0]
print("Even numbers:", even_numbers)

# Exercise 2: List every 2nd number in the list
every_second_number = numbers[1::2]  # Start from the second element and step by two
print("Every second number:", every_second_number)

# Exercise 3: List every odd number while the value is under 150
odd_numbers_under_150 = [num for num in numbers if num % 2 != 0 and num < 150]
print("Odd numbers under 150:", odd_numbers_under_150)
