'''
    This module provides sum_with_filter function,
    which sums all numbers with or without a filter.
'''

def sum_with_filter(numbers, filter_function=None):
    '''
        The function sums all numbers that passed filter_function.
        If there is no filter, the function just returns sum of numbers.
    '''
    if numbers is None or len(numbers) is 0:
        return 0

    result_sum = 0
    if filter_function is not None:
        result_sum = sum(list(filter(filter_function, numbers)))
    else:
        result_sum = sum(numbers)
    return result_sum

def divided_by_3_or_5(number):
    ''' Checks if a number is divisible by 3 or 5. '''
    return number % 3 == 0 or number % 5 == 0

if __name__ == '__main__':
    print(sum_with_filter(range(1, 1000), divided_by_3_or_5))
