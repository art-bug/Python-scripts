'''
    This module has one invert_dict function which swaps dictionary keys and values (inverts it).
    In script mode the module attempts one string argument - dictionary for inverting.
'''

import sys
import ast

def invert_dict(input_dict):
    '''
        The function inverts a dictionary, i.e. swaps keys and values.
        Returns an inverted dictionary.
    '''
    inverted_dict = {value:key for key, value in input_dict.items()}
    return inverted_dict

def __main():
    '''
        Using when file runs as script.
        Example:
            invert_dict.py "{6: 'cd', 'ab': False, 4.5: 5.5, True: 12}" ,
            result - {'cd': 6, False: 'ab', 5.5: 4.5, 12: True}
    '''
    dict_arg = ast.literal_eval(sys.argv[1])
    print(invert_dict(dict_arg))

if __name__ == '__main__':
    __main()
