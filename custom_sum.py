'''
    This module has one custom_sum function,
    which sums all numbers from 1 to 999, which are divided by 3 or 5.
'''

def custom_sum():
    '''
        The function sums all numbers from 1 to 999,
        which are divided by 3 or 5.
    '''
    result = sum([number for number in range(1, 1000)
                  if number % 3 == 0 or number % 5 == 0])
    return result

if __name__ == '__main__':
    print(custom_sum())
