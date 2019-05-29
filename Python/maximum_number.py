def find_maximum_number(numbers):
    max = numbers[0]
    for num in numbers:
        if num > max:
            max = num
    return max
