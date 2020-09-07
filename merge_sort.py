'''
    This module provides merge sort function.
'''

from math import ceil
import sys
import ast

def mergesort(array, ascending=True):
    '''
        The function sorts an array by merge sort
        (default ascending order).
        Returns a sorted array.
    '''
    if not array:
        return array

    if len(array) == 1:
        return array

    left_array = mergesort(array[:ceil(len(array) / 2)], ascending)
    right_array = mergesort(array[ceil(len(array) / 2):], ascending)

    def merge(l_array, r_array):
        result_array = []

        l_arr_idx = 0
        r_arr_idx = 0

        while (l_arr_idx < len(l_array) and r_arr_idx < len(r_array)):
            comparison = l_array[l_arr_idx] < r_array[r_arr_idx] if ascending \
                         else l_array[l_arr_idx] > r_array[r_arr_idx]

            if comparison:
                result_array.append(l_array[l_arr_idx])
                l_arr_idx += 1
            else:
                result_array.append(r_array[r_arr_idx])
                r_arr_idx += 1

        result_array.extend(l_array[l_arr_idx:])
        result_array.extend(r_array[r_arr_idx:])

        return result_array

    return merge(left_array, right_array)

def __main():
    '''
        Using when file runs as script.
        Examples:
            merge_sort.py "[2, 6, 7, 4, 8]" , result - [2, 4, 6, 7, 8]
            merge_sort.py "[2, 6, 7, 4, 8]" False , result - [8, 7, 6, 4, 2]
    '''
    array_arg = ast.literal_eval(sys.argv[1])

    if len(sys.argv) == 2:
        print(mergesort(array_arg))
    else:
        sort_order = ast.literal_eval(sys.argv[2])
        print(mergesort(array_arg, sort_order))

if __name__ == '__main__':
    __main()
