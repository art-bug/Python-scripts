'''
    This module provides count_with_filter function,
    which counts all numbers with or without a filter.
'''

def count_with_filter(numbers, filter_function=None):
    '''
        The function counts all numbers that passed filter_function.
        If there is no filter, the function just returns count of numbers.
    '''
    if numbers is None or len(numbers) is 0:
        return 0

    result_count = 0
    if filter_function is not None:
        result_count = len(list(filter(filter_function, numbers)))
    else:
        result_count = len(numbers)
    return result_count

def digits_diff_ge_3(number):
    '''
        Checks that the difference between the digits of a number is
        not less (i.e. greater or equal) than 3.
    '''
    str_number = str(number)
    
    # If number digits are same
    if str_number[1:] == str_number[:-1]:
        return False

    # Get sorted number digits
    number_digits = list(map(int, sorted(str_number)))

    return (number_digits[1] - number_digits[0] >= 3) and \
           (number_digits[-1] - number_digits[1] >= 3)

if __name__ == '__main__':
    print(count_with_filter(range(100, 1000), digits_diff_ge_3))
