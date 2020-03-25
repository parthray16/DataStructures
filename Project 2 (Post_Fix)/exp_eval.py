"""
CPE202
Project 2

Author:
    Parth Ray
"""
from stacks import StackLinked

def infix_to_postfix(infix_expr):
    """converts an infix expression into a postfix expression
    Args:
        infix_expr (str): expression in infix notation only consisting of
                          numbers (integers, reals, positive or negative),
                          parentheses, and the operators separated by spaces.
    Returns:
        String: the postfix converted infix expression
    """
    operators = {"*": 3, "/": 3, "+": 2, "-": 2, "^": 4, "~": 4, "(": 1}
    operator_stack = StackLinked()
    post_fix = []
    infix = infix_expr.split()
    for i in infix:
        if is_number(i):
            post_fix.append(i)
        elif i == "(":
            operator_stack.push(i)
        elif i == ")":
            item = operator_stack.pop()
            while item != "(":
                post_fix.append(item)
                item = operator_stack.pop()
        else:
            while not operator_stack.is_empty() and \
                (operators[operator_stack.peek()] > operators[i]):
                post_fix.append(operator_stack.pop())
            operator_stack.push(i)
    while not operator_stack.is_empty():
        post_fix.append(operator_stack.pop())
    return " ".join(post_fix)


def postfix_eval(postfix_expr):
    """evaluates a postfix expression into a value. Uses the postfix_valid function described
       below to check the validity of the expression
    Args:
        postfix_expr (str): an expression in postfix notation
    Returns:
        int/float: the solution to the postfix expression if valid
    Raises:
        SyntaxError: when the postfix expression is invalid
        ZeroDivisionError: when dividing by zero
    """
    if not postfix_valid(postfix_expr):
        raise SyntaxError
    expr = postfix_expr.split()
    operands_stack = StackLinked()
    for i in expr:
        if is_number(i):
            operands_stack.push(float(i))
        elif i == "^":
            exp = operands_stack.pop()
            item = operands_stack.pop() ** exp
            operands_stack.push(item)
        elif i == "*":
            item = operands_stack.pop() * operands_stack.pop()
            operands_stack.push(item)
        elif i == "/":
            div = operands_stack.pop()
            if div == 0:
                raise ZeroDivisionError
            item = operands_stack.pop() / div
            operands_stack.push(item)
        elif i == "+":
            item = operands_stack.pop() + operands_stack.pop()
            operands_stack.push(item)
        elif i == "-":
            sub2 = operands_stack.pop()
            item = operands_stack.pop() - sub2
            operands_stack.push(item)
        elif i == "~":
            item = operands_stack.pop() * -1
            operands_stack.push(item)
    return round(operands_stack.pop(), 2)


def postfix_valid(postfix_expr):
    """to test for an invalid postfix expression
    Args:
        postfix_expr (str): an expression in postfix notation
    Returns:
        Boolean: True if valid postfix expression (proper number of operands
                 and operators in valid positions), False otherwise
    """
    post_fix = postfix_expr.split()
    valid = 0
    for i in post_fix:
        if is_number(i):
            valid += 1
        elif i in "+-*/^":
            valid -= 2
            if valid < 0:
                return False
            valid += 1
        elif i == "~":
            valid -= 1
            if valid < 0:
                return False
            valid += 1
    if valid == 1:
        return True
    return False


def is_number(token):
    """tells if token string is a number
    Args:
        token (str): any string token
    Returns:
        Boolean: True if token is number, false if otherwise
    """
    try:
        float(token)
        return True
    except ValueError:
        return False
