"""
CPE202
Project 2 Test File

Author:
    Parth Ray
"""
import unittest
from exp_eval import infix_to_postfix, postfix_eval, postfix_valid

class TestCase(unittest.TestCase):
    def test_infix_to_postfix(self):
        self.assertEqual(infix_to_postfix("~ 3 ^ 2"), "3 2 ^ ~")
        infix = open("sample_infix_expressions.txt", "r")
        postfix = open("sample_postfix_expressions.txt", "r")
        in_line = infix.readline().strip()
        post_line = postfix.readline().strip()
        while in_line != "":
            self.assertEqual(infix_to_postfix(in_line), post_line)
            in_line = infix.readline().strip()
            post_line = postfix.readline().strip()
        infix.close()
        postfix.close()

    def test_postfix_eval(self):
        self.assertEqual(postfix_eval("4 5 6 * +"), 34)
        self.assertRaises(SyntaxError, postfix_eval, "3 * +")
        self.assertRaises(ZeroDivisionError, postfix_eval, "3 5 5 - /")
        self.assertEqual(postfix_eval("3 2 ^ ~"), -9)
        self.assertEqual(postfix_eval("3 ~ 2 ^"), 9)
        self.assertEqual(postfix_eval("3 4 5 + * 2 /"), 13.5)
        self.assertEqual(postfix_eval("3 ~ 2 ^ 9 +"), 18)
        self.assertEqual(postfix_eval("5 3 - 2 ^ 4 2 - 2 ^ + 1 2 / ^"), 2.83)
        self.assertEqual(postfix_eval("5.3 7.6 - 1 +"), -1.30)

    def test_postfix_valid(self):
        self.assertEqual(postfix_valid("1 2 3 +"), False)
        self.assertEqual(postfix_valid("15 7 1 1 + - / 3 * 2 1 1 + + -"), True)
        self.assertEqual(postfix_valid("~ 10"), False)
        self.assertEqual(postfix_valid(""), False)
        postfix = open("sample_postfix_expressions.txt", "r")
        for i in postfix:
            self.assertEqual(postfix_valid(i.strip()), True)
        postfix.close()

def main():
    unittest.main()

if __name__ == "__main__":
    main()
