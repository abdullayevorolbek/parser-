def multiply_numbers(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

numbers_list = [3, 5, 7, 2, 4]
result = multiply_numbers(numbers_list)
print(f"The product of numbers {numbers_list} is: {result}")
