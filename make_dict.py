import sys
import ast
import unittest

def make_dict(key_list, value_list):
    if not ((key_list and value_list) or key_list):
        return {}

    result_dict = {}

    if len(key_list) <= len(value_list):
        result_dict = dict(list(zip(key_list, value_list)))
    else:
        new_value_list = value_list + [None for none in range(len(value_list), len(key_list))]
        result_dict = dict(list(zip(key_list, new_value_list)))

    return result_dict

class TestMakeDictFrom(unittest.TestCase):

    def test_equal_length(self):
        result_dict = make_dict([6, "ab", 4.5, True], ["cd", False, 5.5, 12])

        self.assertDictEqual(result_dict, {6: "cd", "ab": False, 4.5: 5.5, True: 12})

    def test_key_list_length_less_than_value_list_length(self):
        result_dict = make_dict([6, "ab"], ["cd", False, 5.5, 12])

        self.assertDictEqual(result_dict, {6: "cd", "ab": False})

    def test_key_list_length_greater_than_value_list_length(self):
        result_dict = make_dict([6, "ab", 4.5, True], ["cd", False])

        self.assertDictEqual(result_dict, {6: "cd", "ab": False, 4.5: None, True: None})

    def test_key_list_is_empty(self):
        result_dict = make_dict([], ["cd", False, 5.5, 12])

        self.assertDictEqual(result_dict, {})

    def test_value_list_is_empty(self):
        result_dict = make_dict([6, "ab", 4.5, True], [])

        self.assertDictEqual(result_dict, {6: None, "ab": None, 4.5: None, True: None})

    def test_key_list_and_value_list_are_empty(self):
        result_dict = make_dict([], [])

        self.assertDictEqual(result_dict, {})

if __name__ == '__main__':
    key_list_arg = ast.literal_eval(sys.argv[1])
    value_list_arg = ast.literal_eval(sys.argv[2])
    print(make_dict(key_list_arg, value_list_arg))
