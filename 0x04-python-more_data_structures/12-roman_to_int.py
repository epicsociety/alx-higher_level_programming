#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or not isinstance(roman_string, str):
        return 0
    my_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    numbers = [my_dict[x] for x in roman_string]
    return numbers[-1] + sum([n * -1 if numbers[idx + 1] > n else n
                             for idx, n in enumerate(numbers[:-1])])
